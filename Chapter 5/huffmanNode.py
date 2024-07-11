import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(characters, frequencies):
    heap = [HuffmanNode(characters[i], frequencies[i]) for i in range(len(characters))]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    root = heap[0]
    huffman_code = {}
    
    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            huffman_code[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    
    generate_codes(root, "")
    return sorted(huffman_code.items())


characters1 = ['a', 'b', 'c', 'd']
frequencies1 = [5, 9, 12, 13]
print("7) ",huffman_codes(characters1, frequencies1)) 
