"""Plot empirical runtime or space usage for the linked-list (a.py) and
skip-list (b.py) implementations.

Usage:
    python3 graph.py --metric runtime --operation search
    python3 graph.py --metric space --structure skip --sizes 100 1000 10000
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from a import LinkedList
from b import SkipList

LABELS = {"linked": "Linked List", "skip": "Skip List"}
COLORS = {"linked": "tab:blue", "skip": "tab:orange"}
RUNTIME_TITLES = {
    "insert": "Insertion",
    "search": "Search",
    "both": "Insertion + Search",
}


def new_structure(name: str, args) -> LinkedList | SkipList:
    if name == "linked":
        return LinkedList()
    return SkipList(max_level=args.max_level, p=args.p)


def count_pointers(structure, name: str) -> int:
    if name == "linked":
        node, total = structure.root, 0
        while node is not None:
            total += 1
            node = node.next
        return total

    node, total = structure.sentinel.next[0], 0
    while node is not None:
        total += node.level
        node = node.next[0]
    return total


def measure(name: str, n: int, args) -> float:
    values = random.sample(range(n * 10), n)
    queries = random.sample(values, min(n, 200))

    if args.metric == "space":
        structure = new_structure(name, args)
        for value in values:
            structure.insert(value)
        return count_pointers(structure, name)

    total = 0.0
    for _ in range(args.trials):
        structure = new_structure(name, args)
        if args.operation == "search":
            for value in values:
                structure.insert(value)

        start = time.perf_counter()
        if args.operation in ("insert", "both"):
            for value in values:
                structure.insert(value)
        if args.operation in ("search", "both"):
            for value in queries:
                structure.search(value)
        total += time.perf_counter() - start

    return total / args.trials


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--structure", choices=["linked", "skip", "both"], default="both"
    )
    parser.add_argument("--metric", choices=["runtime", "space"], default="runtime")
    parser.add_argument(
        "--operation", choices=["insert", "search", "both"], default="both"
    )
    parser.add_argument(
        "--sizes", type=int, nargs="+", default=[100, 500, 1000, 2000, 5000, 10000]
    )
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--max-level", type=int, default=16)
    parser.add_argument("--p", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    structures = ["linked", "skip"] if args.structure == "both" else [args.structure]
    results = {
        name: [measure(name, n, args) for n in args.sizes] for name in structures
    }

    fig, ax = plt.subplots(figsize=(7, 5))
    for name, values in results.items():
        ax.plot(args.sizes, values, marker="o", color=COLORS[name], label=LABELS[name])

    ax.set_xlabel("Number of elements (n)")
    if args.metric == "space":
        ax.set_ylabel("Total nodes")
        ax.set_title("Space Overhead vs. Input Size")
    else:
        ax.set_ylabel("Time (seconds)")
        ax.set_title(f"{RUNTIME_TITLES[args.operation]} Runtime vs. Input Size")
    if args.metric == "runtime":
        ax.set_ylim(0, 0.015)
        ax.set_yticks([0, 0.005, 0.01, 0.015])
    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout()

    output = (
        args.output
        or Path(__file__).resolve().parent.parent.parent
        / "img"
        / f"{args.operation}_{args.metric}.png"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=150)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
