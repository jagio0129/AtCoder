N, M = map(int,input().split())
people = [list(map(int, input().split())) for _ in range(N)]
most_list = []

for i,p in enumerate(people):
    if i == 0:
        most_list = p[1:]
        continue
    tmp = []
    for j in range(1, len(p)):
        if p[j] in most_list:
            tmp.append(p[j])
    if len(tmp) == 0:
        print(0)
        exit()
    most_list = tmp
print(len(most_list))