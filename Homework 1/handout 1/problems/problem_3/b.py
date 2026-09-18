import collections
import heapq


class Node:
    """Node used to build the Huffman tree."""

    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_compress(all_rle_symbols):
    """
    Generates Huffman codes and encodes a stream of RLE symbols.

    Args:
        all_rle_symbols (list[tuple]): A list of all RLE symbols from an entire image.

    Returns:
        tuple[dict, str]: A tuple containing:
            - A dictionary mapping each unique RLE symbol to its Huffman code.
            - The fully encoded data as a single binary string.
    """
    if not all_rle_symbols:
        return {}, ""

    # 1. Calculate frequency of each RLE symbol. `collections.Counter` is useful.
    # 2. Build the Huffman tree using a priority queue. `heapq` is recommended.
    # 3. Traverse the tree to generate Huffman codes.
    # 4. Encode `all_rle_symbols` into a single bitstring using your codes.
    huffman_codes = {}
    encoded_data = ""
    
    frequency_counts = collections.Counter(all_rle_symbols)
    
    heap = []
    
    
    for item, count in frequency_counts.items():
        heapq.heappush(heap, Node(item, count))
        
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = Node(None, left.freq + right.freq, left, right)
        
        heapq.heappush(heap, parent)
        
    root = heap[0]
    huffman_codes = create_huffman_tree(root, "", huffman_codes)
    
    for symbol in all_rle_symbols:
        encoded_data += huffman_codes[symbol]
        
    return huffman_codes, encoded_data

def create_huffman_tree(node, code, codes):
    if node is None:
        return codes

    if node.left is None and node.right is None:
        codes[node.symbol] = code if code else "0"
        return codes

    create_huffman_tree(node.left, code + "0", codes)
    create_huffman_tree(node.right, code + "1", codes)

    return codes