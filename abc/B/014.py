# https://atcoder.jp/contests/abc014/tasks/abc014_2
n, X = map(int, input().split())
prices = list(map(int, input().split()))
b = bin(X).split("0b")[1].zfill(n)
sum = 0
for i,s in enumerate(b):
    if s == '1':
        sum += prices[len(b)-i-1]
print(sum)