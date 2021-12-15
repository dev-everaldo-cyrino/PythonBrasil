a = 1
b = 1
c = 0
n = []
n.append(b)
while a < 10000000000:
    n.append(a)
    c = a
    a += b
    b = c
    
print(n)