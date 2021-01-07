#include <iostream>

int main()
{
  int * iptr;

  iptr = new int[536870911]; // 配置超大的陣列
                             // 將引發例外
  delete[] iptr;
  std::cout << "發生例外時看不見這行訊息！\n";
}
