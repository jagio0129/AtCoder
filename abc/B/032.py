S = str(input())
k = int(input())
ary = []
for i in range(len(S)):
    s = S[i:i+k]
    if len(s) < k or s in ary:
        continue
    ary.append(s)
print(len(ary))