#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s, target = "book", ins = "the ";
  cout << "請輸入一個字串：";
  getline(cin, s);

  unsigned int i, pos = 0;
  while ((i = s.find(target,pos))!=string::npos) {
    s.insert(i,ins);  // 在搜尋到 target 的位置插入 ins 字串
    pos = i + ins.size() + 1;    // 從原找到的位置之後繼續找
  }

  cout << "新字串：" << s;
}
