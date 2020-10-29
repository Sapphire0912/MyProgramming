#include<iostream>
using namespace std;

int main()
{
  float f_pi;
  double d_pi;
  // 將圓周率值指定給變數
  f_pi  = 3.1415926535897932f;
  d_pi  = 3.1415926535897932;

  cout.precision(17);
  cout << "f_pi = "  << f_pi  << endl
       << "d_pi = "  << d_pi  << endl;
}
