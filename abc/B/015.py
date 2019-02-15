import math 
N = int(input())
bugs = list(map(int, input().split()))
bug_soft = 0
sum_bugs = 0
for b in bugs:
    if b > 0:
        bug_soft += 1
        sum_bugs += b
print(math.ceil(sum_bugs/bug_soft))