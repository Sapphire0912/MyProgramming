#include<iostream>
using namespace std;

class Flyable {      // 飛行的『介面』
public:
  virtual void takeoff() =0; // 起飛
  virtual void flying()  =0; // 飛行
  virtual void landing() =0; // 降落
};

class Bird : public Flyable {       // 鳥
public:
  void takeoff() { cout << "張開翅膀, 揮動翅膀" << endl; }
  void flying()  { cout << "展翅滑翔, 揮翅加速" << endl; }
  void landing() { cout << "兩腳前伸, 收翅落地" << endl; }
};

class Jetplane : public Flyable {   // 噴射機
public:
  void takeoff() { cout << "加油門, 仰起, 收起落架" << endl; }
  void flying()  { cout << "加油門" << endl; }
  void landing() { cout << "減速, 放起落架, 著地" << endl; }
};

int main()
{
  Bird egale;
  cout << "egale 的飛行歷程：" << endl;
  egale.takeoff();
  egale.flying();
  egale.landing();

  Jetplane airbus;
  cout << "airbus 的飛行歷程：" << endl;
  airbus.takeoff();
  airbus.flying();
  airbus.landing();
}
