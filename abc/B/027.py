# https://atcoder.jp/contests/abc027/tasks/abc027_b
N = int(input())
p = list(map(int, input().split()))

if not sum(p) % N == 0:
    print(-1)
    exit()
else:
    ary, ary2 = [], []
    ave = sum(p) // N
    for i in range(len(p)):
        ary.append(p[i])
        if sum(ary) == len(ary) * ave:
            ary2.append(ary)
            ary = []
sum = 0
for a in ary2:
    sum += len(a)-1
print(sum)