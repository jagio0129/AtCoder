n, m = map(int, input().split())
n %= 12
# 長針
l = 6 * m
# 短針
s = l/12+n*30
print(min(abs(l-s),360-abs(l-s)))