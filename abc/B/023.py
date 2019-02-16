N = int(input())
S = str(input())
logo = "b"
cnt = 0

def can_make(logo):
    if S == logo:
        print(cnt)
        exit()

if S == logo:
    print(0)
    exit()

while len(logo) <= len(S):
    cnt += 1
    if cnt % 3 == 1: 
        logo = "a" + logo + "c"
        can_make(logo)
    elif cnt % 3 == 2:
        logo = "c" + logo + "a"
        can_make(logo)
    else:
        logo = "b" + logo + "b"
        can_make(logo)
print(-1)