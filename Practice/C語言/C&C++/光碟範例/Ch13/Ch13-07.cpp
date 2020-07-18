#include<iostream>
using namespace std;

class AA {
public:
  int geti() {return i;}
  void seti(int i) { this->i = i; }
protected:
  int i;
};

class BB : virtual public AA {   // AA 為虛擬基礎類別
};

class CC : virtual public AA {   // AA 為虛擬基礎類別
public:
  void seti(int i) { this->i *= i; }  // 蓋掉 AA 的同名函式
};

class DD : public BB, public CC {     // 多重繼承
public:
  DD (int i=100) { this-> i = i; }
};

int main()
{
  DD d;
  d.seti(33);        // 將會呼叫 CC::seti(33)
  cout << d.geti() << endl;
  d.BB::seti(33);    // 強制經由 BB 呼叫 AA::seti(33)
  cout << d.geti() << endl;
}
