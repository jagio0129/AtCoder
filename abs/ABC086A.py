a,b = map(int, input().split())

t = a*b
if t % 2 == 0:
    print('Even')
else:
    print('Odd')