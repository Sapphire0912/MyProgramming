# 輸入 西元年月日, 計算為當年的第幾天

def whichdays(day):
    # 先判斷閏年
    year = day // 10000
    x = 0
    if year % 4 == 0:
        if year % 400 == 0:
            x = 1
        elif year % 100 == 0:
            x = 0

    month = day % 10000 // 100
    days = day % 100

    if month > 12:
        raise ValueError("該日期格式錯誤")

    # 該年每個月的天數
    if x:
        if month == 2 and days > 29:
            raise ValueError("閏年2月不能大於29天")
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if days > months[month-1]:
            raise ValueError("該日期格式錯誤")
    else:
        if month == 2 and days > 28:
            raise ValueError("非閏年2月不能大於28天")
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if days > months[month-1]:
            raise ValueError("該日期格式錯誤")

    total = sum(months[:month-1]) + days
    return total

try:
    s = int(input("輸入西元年月日(Ex: 20001002): "))
    if s < 0:
        raise TypeError
except TypeError:
    print("The number does not match the format.")
except ValueError:
    print("The number is not an integer.")
else:
    day = whichdays(s)
    print(s, "為 該年的第", day, "天")
