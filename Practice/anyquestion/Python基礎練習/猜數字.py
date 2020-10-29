import time as t
import random
print("1A2B遊戲規則:")
print("    遊戲一開始電腦會隨機從0~9共十個數字中選出4個不重複的數字由左而右排列，玩家須猜這四個數字。")
print("玩家猜測數字後，會顯示XAXB(A代表數字正確且位置正確，B為數字正確但位置錯誤)，\
遊戲會進行到玩家猜測出正確的數字串。過程中會計算遊戲持續的時間，並在遊戲結束時給予玩家文字鼓勵並告知耗時時間。")
print("以上為1A2B的遊戲規則，若要開始遊戲請輸入Y/y, 若要離開遊戲請輸入除了y的任意鍵")

# com OK
def com():
    allmath = '0123456789'
    rep = []
    while len(rep) < 4:
        num = random.choice(allmath)
        if num in rep:
            del rep[-1]
        else:
            rep.append(num)
    return rep

# check OK
def check(guess):
    for num in guess:
        if num == " ":
            print("格式錯誤: 輸入包含空白字符")
            return False
        elif ord(num) > 57 or ord(num) < 48:
            lower, upper = 65, 97
            eng = []
            for i in range(26):
                eng.append(chr(lower + i))
                eng.append(chr(upper + i))
            if num in eng:
                print("格式錯誤: 輸入包含英文字母")
                return False
            else:
                print("格式錯誤: 輸入包含非法字符")
                return False
    
    isrep = list(guess)
    for number in isrep:
        for i in range(4):
            if isrep.index(number) == i:
                continue
            elif isrep[i] == number:
                print("格式錯誤: 輸入包含重複的數字")
                return False
    return True

def process(user_guess, com_numbers):
    count_A, count_B = 0, 0
    for i in range(4):
        if user_guess[i] in com_numbers:
            if i == com_numbers.index(user_guess[i]):
                count_A += 1
            else:
                count_B += 1
    if count_A != 4:
        print("{}A{}B".format(count_A, count_B))
    else:
        return True

# playing OK
def playing(numbers):
    while True:
        guess = input("請輸入你要猜的數字: ")
        if len(guess) != 4:
            print("格式錯誤: 輸入的字串不等於4個字")
        elif check(guess):
            if process(list(guess), numbers):
                print("恭喜答對!")
                break
    time_end = t.localtime()[3:6]
    return time_end

# main OK
def main():
    start = input()
    if start == 'Y' or start == 'y':
        print("計時開始!") # 等等放入計時
        t_start = t.localtime()[3:6]
        s = com()
        t_end = playing(s)
        hr = t_end[0] - t_start[0]
        min = t_end[1] - t_start[1]
        sec = t_end[2] - t_start[2]
        tu = (hr, min, sec)
        print("總共花了%02d時%02d分%02d秒" %tu)
    else:
        print("離開遊戲")

main()