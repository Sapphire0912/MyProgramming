#include<iostream>
using namespace std;

int main()
{
  unsigned int i;  // 變數 i 只能記錄正整數或 0
  short j;  // 省略 "int" 關鍵字
  long  k;  // 省略 "int" 關鍵字
  unsigned long  l;  // 省略 "int" 關鍵字
  i = 1999;
  j = 32767;
  k = 2147483648;  // 故意設為 long 最大值加 1
  l = 4294967295;
  cout << i << ' ' << j << ' ' << k << ' ' << l << endl;
}
