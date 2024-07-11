def stairs(n):
    if n == 0 or n == 1:
        return 1    
    p1, p2 = 1, 1
    for i in range(2, n + 1):
        current = p1 + p2
        p2 = p1
        p1 = current    
    return p1
print(stairs(4)) 
print(stairs(3))