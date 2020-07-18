#include<iostream>
using namespace std;

class AA {
protected:
  int i;
};

class BB : virtual public AA {}; // AA 為虛擬基礎類別
class CC : virtual public AA {}; // AA 為虛擬基礎類別

class DD : public BB, CC {       // 以私有方式繼承 CC
public:
  DD (int i=100) { this-> i = i; }
  int geti() {return i;}
  void change()
  {
    i = -1000;  // 可存取到虛擬基礎類別的 protected 成員
  }
};

int main()
{
  DD d;
  d.change();
  cout << d.geti() << endl;
}
