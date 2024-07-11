def decode_huffman(characters, frequencies, encoded_string):
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
    decoded_string = ""
    current_node = root
    
    for bit in encoded_string:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = root
    
    return decoded_string


characters1 = ['a', 'b', 'c', 'd']
frequencies1 = [5, 9, 12, 13]
encoded_string1 = '1101100111110'
print("8) ",decode_huffman(characters1, frequencies1, encoded_string1)) 
