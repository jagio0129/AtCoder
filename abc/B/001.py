m = int(input())
km = m/1000
VV = ""
if km < 0.1:
    VV = "00"
elif 0.1 <= km <= 5:
    VV = str(int(km*10)).zfill(2)
elif 6 <= km <= 30:
    VV = str(int(km + 50))
elif 35 <= km <= 70:
    VV = str(int((km-30)/5 + 80))
elif 70 < km :
    VV = "89"
print(VV)
