#include<iostream>
using namespace std;

class AA {
public:
  int geti() {return i;}
  void seti(int i) { this->i = i; }
protected:
  int i;
};

class BB : public AA {}; // 繼承 AA
class CC : public AA {}; // 繼承 AA

class DD : public BB, public CC {}; // 多重繼承 BB、CC

int main()
{
  DD d;
  d.BB::seti(10);               // 呼叫 BB 中的成員函式
  d.CC::seti(8);                // 呼叫 CC 中的成員函式
  cout << d.BB::geti() << endl; // 呼叫 BB 中的成員函式
  cout << d.CC::geti() << endl; // 呼叫 CC 中的成員函式
}
