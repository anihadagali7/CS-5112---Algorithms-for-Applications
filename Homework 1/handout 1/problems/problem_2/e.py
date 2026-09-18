"""
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
"""

def interval_covering(M: int, intervals: list) -> list:
    J = []
    for interval in intervals:
        J.append([interval[0], interval[1]])

    while True:
        earliest_redundant = -1

        for i in range(len(J)):
            others = []
            for j in range(len(J)):
                if j != i:
                    others.append(J[j])

            start = J[i][0]
            finish = J[i][1]

            if is_covered_by_others(others, start, finish):
                if earliest_redundant == -1:
                    earliest_redundant = i
                elif finish < J[earliest_redundant][1]:
                    earliest_redundant = i

        if earliest_redundant == -1:
            break

        J.pop(earliest_redundant)

    return J


def is_covered_by_others(others, a, b):
    covered_until = a

    while covered_until < b:
        farthest = covered_until

        for interval in others:
            start = interval[0]
            end = interval[1]
            if start <= covered_until and end > farthest:
                farthest = end

        if farthest == covered_until:
            return False

        covered_until = farthest

    return True
