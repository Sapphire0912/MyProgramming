import sqlite3

# 開啟資料庫
def opendb():
    lib_path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\教學\\Ch03 資料庫應用_智力問答測試\\students.db"
    conn = sqlite3.connect(lib_path)
    cur = conn.cursor()
    cur.execute("create table if not exists addressbook(usernum integer primary key, \
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
def into():
    usernum = input("請輸入學號: ")
    username = input("請輸入姓名: ")
    passworld = input("請輸入身分證: ")
    address = input("請輸入地址: ")
    telnum = input("請輸入連絡電話: ")
    return usernum, username, passworld, address, telnum

# 在資料庫中增加內容
def adddb():
    print("----------增加資料功能----------")
    person = into()
    hel = opendb()
    hel[1].execute("insert into addressbook(usernum, username, passworld, address, telnum) values(?, ?, ?, ?, ?)", (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print("----------新增資料成功----------")
    showalldb()
    hel[1].close()

# 刪除資料庫中的內容
def deldb():
    print("----------刪除資料功能----------")
    delchoice = input("請輸入要刪除的學號: ")
    hel = opendb()
    hel[1].execute("delete from addressbook where usernum = " + delchoice)
    hel[1].commit()
    print("----------刪除資料成功----------")
    showalldb()
    hel[1].close()

# 修改資料庫的內容
def alter():
    print("----------修改資料功能----------")
    change = input("請輸入要修改的學生學號: ")
    hel = opendb()
    person = into()
    hel[1].execute("update addressbook set usernum = ?, username = ?, passworld = ?, address = ?, telnum = ? where usernum = " + change, 
    (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    showalldb()
    hel[1].close()

# 查詢資料
def search():
    print("---------查詢資料功能----------")
    choice = input("請輸入要查詢學生的學號: ")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from addressbook where usernum = " + choice)
    hel[1].commit()
    print("----------目標資料如下----------")
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    hel[1].close()

# 操作介面, 以及是否繼續操作
def conti(a):
    choice = input("是否繼續? (y or n): ")
    if choice == 'y':
        a = 1
    if choice == 'n':
        a = 0
    return a

flag = 1
while flag:
    print("----------資料庫通訊錄----------")
    choiceshow = """
    請選擇你的進一步選擇:
    1 增加資料
    2 刪除資料
    3 修改資料
    4 查詢資料
    請選擇要進行的操作:
    """
    choice = int(input(choiceshow))
    if choice == 1:
        adddb()
        flag = conti(flag)
    if choice == 2:
        deldb()
        flag = conti(flag)
    if choice == 3:
        alter()
        flag = conti(flag)
    if choice == 4:
        search()
        flag = conti(flag)
    else:
        print("輸入錯誤, 重新輸入")