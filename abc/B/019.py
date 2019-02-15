# https://atcoder.jp/contests/abc019/tasks/abc019_2
import itertools

s = str(input())
v = ""
gr = itertools.groupby(s)
for key,group in gr:
    v += "%s%d" % (key,len(list(group)))
print(v)