n = int(input())
tri = [0,0,1]
for i in range(n-3):
    a = tri[i]+tri[i+1]+tri[i+2]
    a %= 10007
    tri.append(a)
print(tri[n-1])