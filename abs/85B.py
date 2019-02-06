N = int(input())
lengths = sorted(set(list(map(int, [input() for i in range(N)]))), reverse=True)
print(len(lengths))