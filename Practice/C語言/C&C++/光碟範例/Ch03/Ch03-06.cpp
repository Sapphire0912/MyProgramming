#include<iostream>
using namespace std;

int main()
{
  char c1, c2;       // 宣告 2 個字元變數
  wchar_t c3;
  c1 = 'a';  // 將字元 'a' 指定給變數
  c2 = 65;   // 將 ASCII 碼 65 的字元指定給變數
  c3 = '大';
  cout << c1 << endl << c2 << endl << c3 << endl;
}
