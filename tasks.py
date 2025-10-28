def f(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

n = int(input().strip())

l = list(map(int, input().split()))
p = [0] + l 
        
v = [False] * (n + 1)
e = 0.0

for i in range(1, n + 1):
    if not v[i]:
        c = 0
        curr = i
        
        while not v[curr]:
            v[curr] = True
            curr = p[curr]
            c += 1
        
        if c > 1:
            e += f(c)

print(f"{e:.6f}")