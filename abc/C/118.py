N = int(input())
hps = sorted(list(map(int, input().split())))

while len(hps) > 1:
    for i in range(1, len(hps)):
        hps[i] = hps[i] % hps[0]
    hps = sorted(set(hps))
    if 0 in hps:
        hps.remove(0)
print(hps[0])