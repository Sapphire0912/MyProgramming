#include <iostream>
using namespace std;
#define  cube(x)   x * x * x   // 計算立方的巨集

int main()
{
  for(int i=1;i<10;i+=2)
    cout << i << " 的三次方等於 "
         << cube(i) << endl;
}
