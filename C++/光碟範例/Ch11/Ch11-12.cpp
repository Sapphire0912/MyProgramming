#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s, target = "0123456789";
  cout << "請輸入一個字串：";
  getline(cin, s);

  unsigned int i, count = 0, pos = 0;
  while ((i = s.find_first_of(target,pos))!=string::npos) {
    count++;       // 計數器加 1
    pos = i + 1;   // 從前次找到的位置之後繼續搜尋
  }

  cout << endl << "在[" << s << "]中";
  if (count == 0)   // 若傳回 npos
    cout << "沒有數字字元！";
  else
    cout << "共有 " << count << " 個數字字元";
}
