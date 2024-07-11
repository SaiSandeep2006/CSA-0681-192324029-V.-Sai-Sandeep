class WordFilter:
    def __init__(self, words):
        self.words = words

    def f(self, pref, suff):
        max_index = -1
        for i in range(len(self.words)):
            if self.words[i].startswith(pref) and self.words[i].endswith(suff):
                max_index = max(max_index, i)
        return max_index
        

# Example of WordFilter Class Usage
wordFilter = WordFilter(["apple"])
output = wordFilter.f("a", "e")
print(output)  