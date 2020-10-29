#include<iostream>
using namespace std;

int main()
{
  cout << true << endl;                 // 使用預設的方式
  cout << boolalpha << false << endl;   // 設為輸出『文字』
  cerr << "cerr：" << true << endl;     // cerr 會不會變？
  cout << true << endl;                 // 試試現在輸出的是？
  cout << noboolalpha << false << endl; // 設為輸出『數字』
}
