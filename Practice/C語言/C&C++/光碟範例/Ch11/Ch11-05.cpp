#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = string(3,'+');  // 建立新字串 "+++"
  s[0] = 'C';                // 修改第 1 個字元

  for (int i=0;i<(int) s.size();i++) // 依序輸出字串中各字元
    cout << s.at(i);
}
