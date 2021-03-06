#include <iostream>
using namespace std;

double newV(double t, double a=9.8, double v0 = 0)
{                     // 兩個參數有預設值
  return v0 + a*t;
}

int main()
{
  cout << "速度與加速度的計算示範：V=V0+at" << endl;

  cout << "若 V0 = 100, a = 2.8, t =15, 則 "
       << "V = " << newV(15,2.8,100) << endl;

  cout << "若 V0 = 0  , a = 9.8, t =15, 則 "
       << "V = " << newV(15);  // 只傳一個參數
}
