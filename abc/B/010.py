# https://atcoder.jp/contests/abc010/tasks/abc010_2
N = int(input())
flowers = list(map(int, input().split()))

def is_love(petals):
    if (petals % 3 != 2) and (petals % 2 == 1):
        return True
    return False

cnt = 0
for petal in flowers:
    while not is_love(petal):
        petal -= 1
        cnt += 1
print(cnt)
        