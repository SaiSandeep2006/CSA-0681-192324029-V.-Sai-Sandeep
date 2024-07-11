from collections import defaultdict
def fourSumCount(A, B, C, D):
    AB_sum = defaultdict(int)
    count = 0
    for a in A:
        for b in B:
            AB_sum[a + b] += 1    
    for c in C:
        for d in D:
            count += AB_sum[-c - d]
    return count
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))  
