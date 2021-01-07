#include <iostream>
using namespace std;

int main()
{
  int a=10, b=20;  // 宣告兩個 int 變數 a, b
  int temp;        // 宣告暫存整數變數 temp

  cout << "交換前 a = " << a << "\tb = " << b << endl;

  temp = a;  // 將變數 a 的值指定給暫存變數
  a = b;     // 把變數 b 的值指定給 a
  b = temp;  // 將暫存變數所存的 a 值指定給 b

  cout << "交換後 a = " << a << "\tb = " << b << endl;
}
