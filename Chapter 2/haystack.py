def str(hay, need):
    if not need:
        return 0
    h= len(hay)
    n= len(need)
    for i in range(h - n + 1):
        if hay[i:i+n] == need:
            return i
    return -1
hay = "sadbutsad"
need = "sad"
print(str(hay, need))