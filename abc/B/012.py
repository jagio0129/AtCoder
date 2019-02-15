N = int(input())

h = N // (60*60)
m = (N - h*60*60) // 60
s = N - h*60*60 - m*60
print("%s:%s:%s" % (str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)))