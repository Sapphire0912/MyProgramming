#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s, s1, s2;
  cout << "請輸入一個字串：";
  getline(cin, s);
  cout << "請輸入要替換掉的字串：";
  getline(cin, s1);
  cout << "要將[" << s1 << "]換成？";
  getline(cin, s2);

  unsigned int i, pos = 0;
  unsigned len1 = s1.size(), len2 = s2.size();
  while ((i = s.find(s1,pos))!=string::npos) {
    s.replace(i,len1, s2); // 將 s1 換成 s2
    pos = i + len2 + 1;    // 從原找到的位置之後繼續找
  }

  cout << "新字串：" << s;
}
