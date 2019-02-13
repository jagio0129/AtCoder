N = int(input())
names = [str(input()) for _ in range(N)]
reader = names[0]
max_vote = 0 
for i in range(len(names)):
    cnt = 0
    for j in range(len(names)):
        if names[i] == names[j]:
            cnt += 1
    if max_vote < cnt:
        max_vote = cnt
        reader = names[i]
print(reader)