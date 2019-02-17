# https://atcoder.jp/contests/abc025/tasks/abc025_b
N,A,B = map(int, input().split())
moves = list(list(input().split()) for _ in range(N))

s = 0
for m in moves:
    m[1] = int(m[1])
    s += (2*(m[0]=="West")-1) * min(max(m[1],A),B)
    
if s < 0:
    print("East", -s)
elif s == 0:
    print(0)
else:
    print("West", s)

'''
# https://atcoder.jp/contests/abc025/tasks/abc025_b
N,A,B = map(int, input().split())
moves = list(list(input().split()) for _ in range(N))
s = 0
for move in moves:
    move[1] = int(move[1])
    if move[0] == "West":
        if move[1] < A:
            s += A
        elif move[1] > B:
            s += B
        else:
            s += move[1]
    if move[0] == "East":
        if move[1] < A:
            s -= A
        elif move[1] > B:
            s -= B
        else:
            s -= move[1]
if s < 0:
    print("East", int(pow(s**2, 1/2)))
elif s == 0:
    print(0)
else:
    print("West", s)
'''