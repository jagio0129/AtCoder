# https://atcoder.jp/contests/abc028/tasks/abc028_b
s=input()
print(*[s.count(x)for x in'ABCDEF'])

'''
from collections import defaultdict
d = defaultdict(int)
S = str(input())
for s in S:
    d[s] += 1
print(d["A"], d["B"], d["C"], d["D"], d["E"], d["F"])
'''