def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f*i
    return f
m = 3
n = 2
a = (m+n-2)-(m-1)
b = m+n-2
c = m-1
print(fact(b)//(fact(c)*fact(a)))