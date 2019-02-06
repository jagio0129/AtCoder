n = int(input())
deck = sorted(list(map(int, input().split())), reverse=True)
alice, bob = 0,0
flag_alice = True
for i in range(len(deck)):
    if flag_alice:
        alice += deck[i]
        flag_alice = False
    else:
        bob += deck[i]
        flag_alice = True
print(alice - bob)