efficted = [500, 200, 100, 50, 20]

def change(dollars):
    coins = [50, 20, 10]
    result = [0, 0, 0]
    for i in range(len(coins)):
        if dollars >= coins[i]:
            count = dollars // coins[i]
            dollars = dollars - count * coins[i]
            result[i] = count
    return result

try:
    dollars = int(input("輸入要兌換的紙鈔: "))
    if dollars >= 0 and dollars % 10 == 0:
        fifty, twenty, ten = change(dollars)
    else:
        raise ValueError
except ValueError:
    print(("The dollars are not efficted."))
else:
    print("Fifty have %d. Twenty have %d. Ten have %d." % (fifty, twenty, ten))