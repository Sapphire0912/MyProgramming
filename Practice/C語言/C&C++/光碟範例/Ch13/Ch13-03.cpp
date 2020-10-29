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
  cout << "AA 佔 " << sizeof(AA) << " 個位元組" << endl;
  cout << "BB 佔 " << sizeof(BB) << " 個位元組" << endl;
  cout << "CC 佔 " << sizeof(CC) << " 個位元組" << endl;
  cout << "DD 佔 " << sizeof(DD) << " 個位元組" << endl;
}
