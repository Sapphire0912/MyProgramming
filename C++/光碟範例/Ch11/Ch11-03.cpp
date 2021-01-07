#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = string();
  cout << "s 的內容：" << s << endl;
  cout << "s 目前容量：" << s.capacity() << endl;

  s.reserve(30);        // 保留空間給 s
  cout << "s 新容量：" << s.capacity() << endl;
  s.reserve(40);        // 保留空間給 s
  cout << "s 新容量：" << s.capacity() << endl;
  cout << "s 的長度為 " << s.size() << '\n' << endl;

  s = "The Hunchback of Notre Dame";
  s.reserve(13);        // 保留小於字串長度的空間
  cout << "reserve(13) 後 s 的內容：" << s << endl;
  s.resize(13);         // 變更大小
  cout << "resize(13)  後 s 的內容：" << s << endl;
  s.resize(150);        // 再把字串變大
  cout << "resize(150) 後 s 的內容：" << s << endl;
  cout<< "s 的長度變成 " << s.size();
}
