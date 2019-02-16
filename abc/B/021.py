# https://atcoder.jp/contests/abc021/tasks/abc021_b

N = int(input())
a, b = map(int,input().split())
K = int(input())
nodes = list(map(int, input().split()))

print("YES" if len(set(nodes))==K and a not in nodes and b not in nodes else "NO") 