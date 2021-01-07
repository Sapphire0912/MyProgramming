#include<iostream>
using namespace std;

class Car {
public:
  Car (double s = 10) { speed = s;}
  double go(double time) { return time * speed;}
private:
  double speed;        // 時速
};

class Ship: private Car {  // 以 private 方式繼承 Car 的成員
public:
  Ship(double s, double c):Car(s) { coff = c; }
  double go(double time, double waterspeed)
  {
    return Car::go(time) + time * waterspeed * coff;
  }
private:
  double coff;   // 水流速度造成船流動速度的係數
};

int main()
{
  Ship s(15,0.4);
  int waterspeed;
  cout << "請輸入目前水流速度？";
  cin >> waterspeed;
  cout << "小船 s 一小時可走 " << s.go(1,waterspeed) << " 公里";
}
