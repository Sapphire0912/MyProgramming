#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s = "longer";

  cout << s.erase(4) << endl;   // 刪除第 5、第 6 個字
  cout << s.erase(2,1) << endl; // 刪除第 3 個字
  cout << "呼叫 erase() 後 s 的容量為：" << s.capacity() << endl;

  s.clear();                    // 清除字串
  cout << "呼叫 clear() 後 s 的內容為：" << s << endl;
}
