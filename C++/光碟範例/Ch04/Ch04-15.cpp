#include<iostream>
using namespace std;

int main()
{
  char   c = 10;
  int    i = 100;
  long   l = 1000;
  float  f = 0.5f;
  double d = 0.5e-10;

  i = (i + f) - (c * i) / d + (l - i) / (f + c) ;
  cout << "i = " << i << endl;
  // 同樣的算式再算一次, 但指定給 double 變數
  d = (i + f) - (c * i) / d + (l - i) / (f + c) ;
  cout << "d = " << d << endl;
}
