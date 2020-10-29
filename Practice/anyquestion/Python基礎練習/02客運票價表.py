locate = ["台北", "桃園", "新竹", "台中", "嘉義", "台南", "高雄"]
kilo = [25, 49, 95, 178, 264, 327, 373]

print("里程表", end = "  ")
for i in range(len(locate)):
    print(locate[i], end = "  ")
print('\n')

for i in range(len(locate)):
    print(" ", locate[i], end = "  ")
    for j in range(len(kilo)):
        km = abs(kilo[i] - kilo[j])
        print("%3d  " % km, end = " ")
    print('\n')

print("價錢表", end = "  ")
for i in range(len(locate)):
    print(locate[i], end = "  ")
print('\n')

for i in range(len(locate)):
    print(" ", locate[i], end = "  ")
    for j in range(len(kilo)):
        km = abs(kilo[i] - kilo[j])
        if km <= 50:
            price = km * 2.5
        if 50 < km <= 200:
            price = km * 2.2
        if  km > 200:
            price = km * 2
        print("%3d  " % price, end = " ")
    print('\n')