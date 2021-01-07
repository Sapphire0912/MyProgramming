#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = "To be or not to be", target;
  cout << "請輸入一字串：";
  cin >> target;

  unsigned int i = s.find(target); // 在 s 中搜尋 target
  if (i == string::npos)   // 若傳回 npos
    cout << "找不到！";
  else                     // 若有找到
    cout << "在[" << s << "]中第一次出現[" << target
         << "]的位置是在第 " << i+1 << " 個字";
}
