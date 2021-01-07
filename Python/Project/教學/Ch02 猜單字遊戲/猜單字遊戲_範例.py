# coding=utf8
# 由電腦隨機產生一個單字, 打亂字母順序, 讓玩家去猜

# 簡單的建立一個單字序列元組
import random
words = ["python", "jumble", "easy", "difficult", "answer", "continue", 'phone', "position", "game", "pose"]

print("猜單字遊戲, 把字母組合成一個正確的單字")
iscontinue = "y"

while iscontinue == "y" or iscontinue == "Y":
    word = random.choice(words)
    correct = word

    jumble = ''
    while word:
        jumble = jumble.join(random.sample(word, len(word)))
        break
    print("亂數後單字: ", jumble)

    while True:
        guess = input("請你猜: ")
        if guess != correct and guess != "":
            print("不正確")
        if guess == correct:
            print("真棒, 猜對了")
            break
    iscontinue = input("是否繼續(Y/N): ")
# Q. 做成 GUI 而且可以連結資料庫的情況或者讀取檔案