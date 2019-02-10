deg, dis = map(int, input().split())
dirs = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW".split()
d = dirs[int(deg + 112.5) // 225 % 16]
 
l = list(map(int,"25 155 335 545 795 1075 1385 1715 2075 2445 2845 3265".split()))
l = [x / 100 * 60 for x in l]
 
w = 0
for x in l:
    if x <= dis: w += 1
    else: break
 
if w == 0: d = "C"
print("{} {}".format(d, w))