N, M = map(int, input().split())
A = [[int(i) for i in input().split()] for i in range(M)]

ans = 0
for i in range(1 << N):
    b = []
    for j in range(1, N + 1):
        if i % 2 == 1:
            b.append(j)
        i //= 2
    
    flag = 1
    for j in range(len(b)):
        for k in range(j + 1, len(b)):
            if [b[j], b[k]] not in A:
                flag = 0
    if flag:
        ans = max(ans, len(b))
    
print(ans)