from typing import List

def full_justify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    line = []
    total_length = 0
    
    for word in words:
        if total_length + len(word) + len(line) > maxWidth:
            for i in range(maxWidth - total_length):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line = []
            total_length = 0
        
        line.append(word)
        total_length += len(word)
    
    result.append(' '.join(line).ljust(maxWidth))
    
    return result

# Example 1
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
output1 = full_justify(words1, maxWidth1)
print(output1)

# Example 2
words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth2 = 16
output2 = full_justify(words2, maxWidth2)
print(output2)
