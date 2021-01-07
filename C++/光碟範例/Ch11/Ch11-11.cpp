#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = "O Romeo, Romeo! wherefore art thou Romeo?", target;
  cout << "要在[" << s << "]中" << "找什麼字？";
  cin >> target;

  unsigned int i, count = 0, pos = string::npos;
  cout << endl << "在[" << s << "]中" << endl;
  while ((i = s.rfind(target,pos))!=string::npos) {
    count++;       // 計數器加 1
    cout << "第 " << count << " 次出現[" << target
         << "]的位置是在第 " << i+1 << " 個字" << endl;
    pos = i - 1;   // 從前次找到的位置之前繼續搜尋
  }

  if (count == 0)   // 若傳回 npos
    cout << "沒有符合[" << target << "]的字串！";
  else
    cout << "總共找到 " << count << " 次";
}
