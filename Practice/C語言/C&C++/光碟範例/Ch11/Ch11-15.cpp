#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s, target = "top";
  cout << "請輸入一個字串：";
  getline(cin, s);

  unsigned int i, pos = 0;
  while ((i = s.find(target,pos))!=string::npos) {
    s.insert(i,1,'s');   // 在搜尋到 target 的位置插入 's'
    pos = i + 2;         // 從原找到的位置之後繼續找
  }

  cout << "新字串：" << s;
}
