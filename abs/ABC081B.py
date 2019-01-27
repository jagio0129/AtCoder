n = input()
m = list(map(int, input().split()))

def simple(m):
    cnt = 0
    allEven = True
    while True:
        for i in range(len(m)):
            if not m[i] % 2 == 0:
                allEven = False
                break
        if allEven:
            cnt += 1
        else:
            break
        m = [int(i/2) for i in m]
    print(cnt)

def shift_bit(m):
    ary = []
    for i in range(len(m)):
        cnt = 0
        b = m[i]
        while b&1 == 0:
            b = b>>1
            cnt += 1
        ary.append(cnt)
    print(min(ary))

simple(m)