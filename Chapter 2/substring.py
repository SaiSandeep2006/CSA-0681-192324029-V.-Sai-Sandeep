def substringWords(words):
    result = set()
    for i in range(len(words)):
        cword = words[i]
        for j in range(len(words)):
            if i != j and cword in words[j]:
                result.add(cword)
                break    
    return list(result)
words = ["mass","as","hero","super hero"]
print(substringWords(words))  