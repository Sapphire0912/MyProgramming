#include <iostream>
using namespace std;

double newV(double t, double a=9.8, double v0 = 0)
{                     // ㄢ把计Τ箇砞
  return v0 + a*t;
}

int main()
{
  cout << "硉籔硉璸衡ボ絛V=V0+at" << endl;

  cout << "璝 V0 = 100, a = 2.8, t =15, 玥 "
       << "V = " << newV(15,2.8,100) << endl;

  cout << "璝 V0 = 0  , a = 9.8, t =15, 玥 "
       << "V = " << newV(15);  // 肚把计
}
