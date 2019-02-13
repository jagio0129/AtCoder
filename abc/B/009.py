N = int(input())
prices = set([int(input()) for _ in range(N)])
print(sorted(prices)[-2])
