def word_break(input_str, word_dict):
    if not input_str:
        return True
    
    n = len(input_str)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and input_str[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

# Dictionary of words
word_dict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}

# Test cases
input_str1 = "ilike"
input_str2 = "ilikesamsung"

output1 = "Yes" if word_break(input_str1, word_dict) else "No"
output2 = "Yes" if word_break(input_str2, word_dict) else "No"

print(f"Input: {input_str1}\nOutput: {output1}")
print(f"Input: {input_str2}\nOutput: {output2}")
