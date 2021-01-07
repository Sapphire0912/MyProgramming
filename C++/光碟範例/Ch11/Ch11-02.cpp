#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s1 = "Object-oriented programming";
  cout << "s1 的容量：" << s1.capacity() << endl
       << "s1 最大可能容量：" << s1.max_size() << endl;

  string s2 = string();
  if (s2.empty())                    // 若 s2 是空字串
    cout << "s2 是空字串" << endl;   // 則輸出訊息
  cout << "s2 的容量：" << s2.capacity() << endl;
}
