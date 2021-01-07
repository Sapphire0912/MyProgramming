#include <iostream>
#include <stdexcept>           // 內含 bad_alloc 類別的宣告
using namespace std;
int main()
{
  int * iptr;

  try {
    iptr = new int[536870911]; // 配置超大的陣列
  }                            // 將引發例外
  catch (bad_alloc e) {
    cerr << "補捉到 std::bad_alloc 例外...\n";
    cerr << e.what();          // 顯示例外的相關訊息
  }

  delete[] iptr;
  cout << "\n發生例外時看不見這行訊息！\n";
}
