L,H = map(int, input().split())
N = int(input())
moves = [int(input()) for _ in range(N)]

for m in moves:
    if m < L:
        print(L-m)
    elif L <= m <= H:
        print(0)
    else:
        print(-1)