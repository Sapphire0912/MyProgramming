#include<iostream>
#include<stdexcept>            // 內含 bad_alloc 類別的宣告
#include<string>
using namespace std;

int main()
{
  string s = "Exception";      // 測試用的字串物件

  try {
    cout << s.at(100);         // 存取超出索引範圍的字元
  }                            // 將引發例外
  catch (bad_alloc e) {
    cerr << "補捉到 std::bad_alloc 例外...\n";
    cerr << e.what();          // 顯示例外的相關訊息
  }

  cout << "\n發生例外時看不見這行訊息！\n";
}
