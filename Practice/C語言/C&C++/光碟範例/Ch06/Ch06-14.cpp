#include <iostream>
#include <cmath>
using namespace std;
#define PI   3.141592653589793     // 定義常數 π

int main()
{
  cout << "角度\tsin()" << endl;

  for(int i=30;i<=180;i+=30) { // 計算 30、60、90...度的正弦函數值
    cout << i << '\t';
    cout << sin(i *PI / 180) << endl;
  }
}
