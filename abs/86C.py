N = int(input())
ary = [list(map(int, input().split())) for i in range(N)]

for t, x, y in ary:
    if (x + y) > t or (x + y + t) % 2 != 0:
        print("YES")
        exit()
print("YES")