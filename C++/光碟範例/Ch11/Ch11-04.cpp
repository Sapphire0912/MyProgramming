#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = string();       // 建立空的字串
  s = "Ilha ";               // 指定新字串內容
  cout << "s 字串：" << s << endl;
  s += "Formosa";            // 附加字串
  cout << "s 字串：" << s << endl;

  s.assign("Life Is Beautiful",8,9); // 從第 8 個字開始,
  cout << "s 字串：" << s << endl;   //   取 9 個字元為新字串
  s.append(" Islander",7);           // 附加參數字串前 7 個字
  cout << "s 字串：" << s << endl;
}
