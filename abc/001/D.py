# hhmm => mmに変換
def hm2mm(time):
    return int(time/100)*60 + int(time%100)

# mmm => hhmmに変換
def mm2hm(time):
    return str(int(time/60)*100 + int(time%60)).zfill(4)

# 開始時間を前に丸める
def r_start(time):
    return int(time) - int(time)%5

# 終了時間を後ろに丸める
def r_end(time):
    return int(time) + int(5-int(time)%5)%5

N = int(input())
times = sorted([input().split("-") for i in range(N)])
imos = [0 for i in range(24*12+1)]

for vs in times:
    # 時間を５分間隔で丸める
    start = r_start(vs[0])
    end   = r_end(vs[1])

    # 分に直す
    start = hm2mm(start)
    end = hm2mm(end)

    # indexに変換する
    si = int(start/5)
    ei = int(end/5)

    # 該当区間を1する
    for i in range(ei-si):
        imos[si+i] = 1

start, end = 0,0
sflag = False
for i in range(len(imos)):
    if (imos[i] == 1) and not sflag:
        start = mm2hm(i*5)
        sflag = True
    if (imos[i] == 0) and sflag:
        end = mm2hm((i-1)*5+5)
        print(start+"-"+end)
        sflag = False