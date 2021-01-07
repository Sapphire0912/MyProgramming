import random
import time

# __all__ = ['gen_func', 'guess']

def gen_func():
    '''隨機產生四位0~9數字, 結果為字串'''
    s = '0123456789'
    com_num = ''.join(random.sample(s, 4))
    return com_num


class handle:
    def __init__(self, com_num):
        '''com_mon: 電腦數字, user_num: 使用者猜測數字, error_text: 異常處理內容,
        result: 電腦要回傳的結果(nAnB), stop: 控制遊戲開始/結束'''
        self.com_num = com_num
        self.user_num = None
        self.error_text = None
        self.result = None
        self.stop = True

    def error(self):
        '''檢查不符合格式的輸入'''
        if len(self.user_num) != 4:
            self.error_text = '輸入的數字長度錯誤!'
        elif not self.user_num.isdigit():
            self.error_text = '輸入內容含非法字元!'
        else:
            for rep in self.user_num:
                if self.user_num.count(rep) != 1:
                    self.error_text = "輸入了重複的數字"
                else:
                    self.error_text = None

    def guess(self, user_num):
        '''使用者猜測數字(輸入為字串)後, 電腦回傳結果'''
        self.user_num = user_num
        self.error()
        A, B = 0, 0
        if not self.error_text:
            for pos in range(len(self.user_num)):
                if self.user_num[pos] in self.com_num:
                    if self.user_num[pos] != self.com_num[pos]:
                        B += 1
                    else:
                        A += 1
            self.result = '%sA%sB' % (A, B)
        else:
            print(self.error_text)

        if A == 4:
            self.stop = False

num = gen_func()
test = handle(num) # call class
print(test.com_num)

while test.stop:
    ip = input("input numbers: ")
    test.guess(ip)
    print(test.result)
print("end.")