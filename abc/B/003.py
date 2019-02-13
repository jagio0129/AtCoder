# https://atcoder.jp/contests/abc003/tasks/abc003_2
S = str(input())
T = str(input())
at = list("@atcoder")
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    elif S[i] == '@' and T[i] in at:
        pass
    elif T[i] == '@' and S[i] in at:
        pass
    else:
        print('You will lose')
        exit()
print('You can win')