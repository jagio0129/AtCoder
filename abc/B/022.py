# https://atcoder.jp/contests/abc022/tasks/abc022_b
N = int(input())
flowers = [int(input()) for _ in range(N)]
print(len(flowers) - len(set(flowers)))