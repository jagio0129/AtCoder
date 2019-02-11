# https://atcoder.jp/contests/abc003/tasks/abc003_1

N = int(input())
sum = 0
for i in range(1, N+1):
    sum += 10000*i
print(int(sum/N))