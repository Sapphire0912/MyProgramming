# 內建雜湊表模組
import hashlib

# Python 建立雜湊表
# 在 Python 使用 字典可以完整呈現雜湊表
# 例如: 建立電話號碼(key-value -> name-phone num)等 需要避免資料重複的資訊

# 雜湊演算法有很多種
# md5, sha1, sha224, sha256, sha384, sha512...etc
# md5 是訊息摘要演算法(Message-Digest Algorithm 5): 被廣泛使用於密碼雜湊
# sha1 安全雜湊演算法(Secure Hash Algorithm): 常被用於數位簽章

# 使用 md5() 方法計算 中文/英文資料的雜湊值
data = hashlib.md5()  # create data object
data.update(b'I am learning Python.')  # update the content of the data object
print("Hash Value: ", data.digest())  # convert data to hash value
print("Hash Value(hex): ", data.hexdigest())
print(type(data))  # print the type of data  # <class '_hashlib.HASH'>
print(type(data.hexdigest()))  # <class 'str'>

# 若要使用中文就要把字串用 utf8 編碼
# s = "正在學習 Python"
# data.update(s.encode('utf-8'))
