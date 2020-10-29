#include <iostream>
using namespace std;

class Destruct {
public:
  Destruct(char ch = ' ')
  {
    c = ch;
    cout << "...呼叫了 " << c << " 的建構函式" << endl;
  }
  ~Destruct()           // 解構函式
  {
    cout << "...呼叫了 " << c << " 的解構函式" << endl;
  }
private:
  char c;
};

Destruct a = 'a';  // 全域物件

void funct()
{
   static Destruct b = 'b'; // 靜態物件
   Destruct c = 'c';        // 局部物件
}

int main()
{
   cout << "程式開始, 先呼叫 funct()" << endl;
   funct();
   cout << "程式結束了！" << endl;
}
