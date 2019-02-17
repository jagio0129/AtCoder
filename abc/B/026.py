# https://atcoder.jp/contests/abc026/tasks/abc026_b
import math
N = int(input())
Rs = sorted([int(input()) for _ in range(N)],reverse=True)
sum = 0
for i,r in enumerate(Rs):
    sum += -(2*(i%2)-1)*(r**2)
print(sum*math.pi)