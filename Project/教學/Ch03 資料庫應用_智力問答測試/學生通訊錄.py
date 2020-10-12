import sqlite3

# 開啟資料庫
def opendb():
    lib_path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\教學\\Ch03 資料庫應用_智力問答測試\\students.db"
    conn = sqlite3.connect(lib_path)
    cur = conn.cursor()
    cur.execute("create table if not exists addressbook(usernum integer primary may, \
                 username varchar(128), passworld varchar(128), address varchar(125), telnum varchar(128))")
    return cur, conn

# 查詢全部資訊
def showalldb():
    print("----------處理後的資料----------")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from addressbook")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h)
        print()
    cur.close()

# 輸入資訊
def info():
    usernum = input("請輸入學號: ")
    username = input("請輸入姓名: ")
    passworld = input("請輸入密碼: ")
    address = input("請輸入地址: ")
    telnum = input("請輸入連絡電話: ")
    return usernum, username, passworld, address, telnum

# 在資料庫中增加內容
# 刪除資料庫中的內容
# 修改資料庫的內容
# 查詢資料
# 操作介面, 以及是否繼續操作
