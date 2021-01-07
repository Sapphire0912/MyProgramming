# sqlite3 教學

# 1. 導入模組
# 2. 建立資料庫連接, 傳回 connection 物件
# 3. 建立游標物件
# 4. 使用 cursor 物件的 execute() 執行 SQL 指令傳回結果集
# 5. 取得游標的查詢結果集
# 6. 資料庫的提交和回復
# 7. 關閉 cursor 物件 和 connection 物件

# 1. 
import sqlite3

# 2. 
# con = sqlite3.connect(connection string) <- connection string 為資料庫的檔案名稱
# lib_path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\教學\\Ch03 資料庫應用_智力問答測試\\database.db"
# con = sqlite3.connect(lib_path)
# 如果該路徑下資料庫存在則開啟, 反之創建

# 3. 
# cur = con.cursor()

# 4.
# cur.execute(sql): 執行 SQL 敘述
# cur.execute(sql, parameters): 執行帶有參數的 SQL 敘述
# cur.executemany(sql, seq_of_pqrameters): 根據參數執行多次 SQL 敘述
# cur.executescript(sql_script): 執行 SQL 指令稿

# 建立一個 category 表
# cur.execute("create table category(id primary key, sort, name)") # 建立了包含 3 個欄位分別為 id, sort, name 的 category 表
# cur.execute("insert into category values(1, 1, 'computer')")
# 在 SQL 敘述字串中可以使用預留位置 "?" 表示參數, 傳遞的參數使用元組
# cur.execute("insert into category values (?, ?, ?)", (2, 2, 'literature'))

# 5.
# cur.fetchone(): 傳回結果集的下一行(Row 物件), 無數據時傳回 None
# cur.fetchall(): 傳回結果集的剩餘行(Row 物件列表), 無數據時傳回 空 List
# cur.fetchmany(): 傳回結果集的多行(Row 物件列表), 無數據時傳回 空 List
# cur.execute("select * from category")
# print(cur.fetchall())

# 也可以用迭代的方式輸出
# for row in cur.execute("select * from category"):
#     print(row[0], row[1])

# 6.
# con.commit() 提交
# con.rollback() 交易復原

# 7. 
# cur.close()
# con.close()


# 建立資料庫和表
# Example: 建立資料庫 sales, 並在其中建立表 book, 表中包含3列, 即 id, price, name, 其中 id 為主鍵(primary key)
lib_path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\教學\\Ch03 資料庫應用_智力問答測試\\sales.db"
# con = sqlite3.connect(lib_path)
# cur = con.cursor()
# cur.execute("create table book(id primary key, price, name)")

# 資料庫的插入, 更新和刪除操作(步驟如下)
# 1. 建立資料庫連接
# 2. 建立游標物件 cursor(), 使用 cur.execute(sql) 來執行 SQL 的 insert, delete, update 等敘述來完成
# 3. 提交操作
# 4. 關閉資料庫

books = [('021', 25, "大學電腦"), ('022', 30, "大學英文"), ('023', 18, "藝術欣賞"), ('024', 25, "程式語言")]
con = sqlite3.connect(lib_path)
cur = con.cursor()

# 插入一行資料
# cur.execute("insert into book(id, price, name) values ('001', 33, '多媒體設計')")
# cur.execute("insert into book(id, price, name) values(?, ?, ?)", ("002", 28, "資料庫基礎"))
# 插入多行資料
# cur.executemany("insert into book(id, price, name) values(?, ?, ?)", books)
# 修改一行資料
# cur.execute("update book set price=? where name=?", (25, "大學英文"))
# 刪除一行資料
# n = cur.execute("delete from book where price=?", (25, )) # 刪除只要價錢是25的所有資料
# print("刪除了", n.rowcount, "行紀錄")
# con.commit()


# 資料庫表的查詢操作
# 1. 建立資料庫連接
# 2. 建立游標並執行 SQL 的 select 敘述
# 3. 循環輸出結果
cur.execute("select id, price, name from book")
for row in cur:
    print(row)

cur.close()
con.close()