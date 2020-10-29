#include<iostream>
#include<iomanip>
using namespace std;
#define pi 3.1415926535897  // ﹚竡盽计

int main()
{
  cout << "箇砞Τ计" << cout.precision() << endl;
  cout << showpoint;      // 砞﹚俱计璶陪ボ计翴
  cout << fixed;          // 计翴ボ猭
  cout << setprecision(8) << 1234.0 << '\t';
  cout << pi << endl;

  cout << scientific;     // 厩才腹ボ猭
  cout << setprecision(4) << 1234.0 << '\t';
  cout << pi << endl;

  cout.precision(8);      // эノΘㄧΑ砞﹚
  cout << scientific << 1234.0 << '\t' << pi << endl;
}
