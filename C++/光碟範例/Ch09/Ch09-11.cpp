#include<iostream>
#include "Ch09-09.h"    // 直接用前面範例的含括檔
using namespace std;

class Account {         // 存款帳戶類別
public:
  Account(char *, double); // 宣告時不用加上成員初始化串列
  void show();
private:
  Str name;             // 帳戶名稱是 Str 類別的物件
  double balance;       // 帳戶餘額
};

Account::Account(char *s, double d) : name(s)
{               // name 成員是在成員初始化串列中設定的
  balance = d;  // 在建構函式內只有指定帳戶餘額
}

void Account::show()
{
  name.show();
  cout << "的帳戶還有 " << balance << " 元";
}

int main()
{
  Account mary("馬力",5000); // 建構帳戶物件
  mary.show();               // 顯示帳戶資訊
}
