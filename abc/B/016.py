A,B,C = map(int, input().split())
print('!+-?'[(A+B==C)+2*(A-B==C)])
