arr=["abc","car","ada","racecar","cool"]
for x in arr:
    if x==x[::-1]:
        print("Palindrome",x)
        break