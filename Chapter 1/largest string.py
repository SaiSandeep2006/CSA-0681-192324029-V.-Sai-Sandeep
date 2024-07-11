def largeGroupPositions(s: str) -> List[List[int]]:
    result = []
    start = 0
    end = 0

    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            if end - start + 1 >= 3:
                result.append([start, end])
            start = i + 1
            end = i + 1

        else:
            end += 1

    return result