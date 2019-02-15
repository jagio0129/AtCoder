# https://atcoder.jp/contests/abc013/tasks/abc013_2
a = int(input())
b = int(input())

d = int((a-b)**2)
d = int(d**(1/2))
print(min(d,10-d))