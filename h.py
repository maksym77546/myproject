n = int(input().strip())

d = list(str(n))
dl = len(d)

m = -1
s = set()

for i in range(1, dl + 1):
    
    st = [(tuple(), d)]

    while st:
        p, r = st.pop()
        
        if len(p) == i:
            
            t = "".join(p)
            
            if len(t) > 1 and t[0] == '0':
                continue
                
            num = int(t)
            
            if num not in s and num <= n:
                s.add(num)
                
                is_p = 0
                
                if num > 1:
                    is_p = 1
                
                if num <= 3 and num > 1:
                    is_p = 1

                if num % 2 == 0 and num > 2:
                    is_p = 0
                
                if num % 3 == 0 and num > 3:
                    is_p = 0
                
                if is_p:
                    j = 5
                    while j * j <= num:
                        if num % j == 0 or num % (j + 2) == 0:
                            is_p = 0
                            break
                        j += 6
                
                if is_p:
                    if num > m:
                        m = num
            
            continue

        for j in range(len(r)):
            
            if j > 0 and r[j] == r[j-1]:
                continue
            
            nx = r[j]
            np = p + (nx,)
            nr = r[:j] + r[j+1:]
            
            st.append((np, nr))

print(m)
