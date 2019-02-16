# https://atcoder.jp/contests/abc024/tasks/abc024_b
N, T = map(int, input().split())
times = [int(input()) for _ in range(N)]
ary = []
for i in range(N-1):
    tmp=times[i+1]-times[i]
    if tmp > T:
        ary.append(T)
    else:
        ary.append(tmp)
ary.append(T)
print(sum(ary))