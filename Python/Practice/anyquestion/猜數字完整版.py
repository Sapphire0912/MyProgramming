# 分為電腦猜玩家/玩家猜電腦
import numpy as np
import random

# 玩家猜電腦
# P1. 玩家先輸入符合規定的數字(回傳一個長度為4的整數列表) <- OK(含防呆)
def first():
    while True:
        try:
            math = input("輸入4個不重複的數字(0~9): ")
            lst = []
            for index in range(0, len(math)):
                lst.append(int(math[index])) # 只要 int 無法轉換也會拋出 ValueError
            if len(lst) != 4:
                raise ValueError
            for i in lst:
                if lst.count(i) > 1:
                    raise ValueError
            return lst
        except ValueError:
            print("輸入數字不符合規定.\n")
            continue


# 電腦猜玩家
# C1. 讓電腦先產生隨機1個整數(回傳一個長度為4的整數列表) <- OK(遞迴去除重複數字)
def cpumath():
    s = '0123456789'
    lst = []
    for i in range(4):
        m = int(random.choice(s))
        lst.append(m)
    
    for i in lst:
        if lst.count(i) > 1:
            del lst
            return cpumath()
    return lst

# C2. 玩家需要輸入結果(格式: nAnB) <- OK(含防呆)(回傳[nA, nB])
def condition():
    Aset = ('A', 'a')
    Bset = ('B', 'b')
    while True:
        try:
            s = input("輸入結果: ")
            if len(s) > 4 or len(s) == 3:
                raise ValueError
            
            # 0A0B 變成 輸入0, 0A3B輸入3B, 1A0B 輸入1A 即可
            length = len(s)
            if length == 1:
                if s[0] == '0':
                    nA, nB = 0, 0
                else:
                    raise ValueError

            if length == 2:
                if s[-1] in Aset:
                    nA, nB = int(s[0]), 0
                if s[-1] in Bset:
                    nA, nB = 0, int(s[0])
                if (s[-1] not in Bset) and (s[-1] not in Aset):
                    raise ValueError

            if length == 4:
                nA, nB = int(s[0]), int(s[2])
            
            # 格式不符合的部分
            if nA + nB > 4 or (nA == 3 and nB == 1):
                raise ValueError
            else:
                return [nA, nB]

        except ValueError:
            print("輸入格式錯誤.\n")
            continue


guessed = [] # 建立電腦已經猜過的數字列表(存放長度為4的列表)
class computer(object):
    # 傳入 nAnB 的地方, count 為猜的次數
    def __init__(self, A, B, count, previous = guessed):
        self.nA = A
        self.nB = B
        self.count = count
        self.guessed = previous
        self.algori = []
    
    def myalgorithm(self):
        # 準備猜第二次的時候無論第一次的結果是甚麼先猜其他的數字(但要先記錄nAnB)
        if self.count == 1: # 猜第二次前 count 依然等於 1
            # 找出剩下的6個數字
            l = self.guessed[0]
            math = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            s = ''
            for i in range(4):
                if l[i] in math:
                    index = math.index(l[i])
                    del math[index]
            for i in math:
                s += str(i)
            
            # 從6個數字裡面隨機選4個
            lst = []
            while True:
                m = int(random.choice(s))
                if m not in lst:
                    lst.append(m)
                if len(lst) == 4:
                    break

            # 紀錄第一次時的結果
            self.algori.append([self.nA, self.nB])

            return lst

    def result(self):
        # 先判斷是否4A了
        if self.nA == 4:
            return True
        return False

       
   
def main():
    print("1A2B猜數字遊戲開始:")
    times = 1 # 計算猜的次數
    lst = cpumath()
    s = ''
    for i in lst:
        s += str(i)

    print("電腦猜的數字: %s" %s)
    guessed.append(lst)
    nA, nB = condition()
    games = computer(nA, nB, times, guessed)

    # 實際上雖然不可能一次就猜中, 為了debug方便還是放一下
    if games.result():
        print("猜了 %d 次猜對了.\n" % times)
    else:
        while True:
            times += 1
            # nextguess 必須放 長度為4的整數列表
            nextguess = games.myalgorithm()
            s = ''
            for i in nextguess:
                s += str(i)
            print("電腦猜的數字: %s" % s)
            guessed.append(nextguess) 
            nA, nB = condition()
            games = computer(nA, nB, times, guessed)

            if games.result():
                print("猜了 %d 次猜對了.\n" % times)
                break
            else:
                continue

main()
print("程式已結束.\n")