#include<iostream>
using namespace std;
#define PI 3.1415926   // 定義巨集常數

int main()
{
  double area;

  // 用巨集常數計算圓面積
  area = 7 * 7 * PI;
  cout << "半徑 7 的圓面積等於 " << area << endl;

  area = 9 * 9 * PI;
  cout << "半徑 9 的圓面積等於 " << area << endl;
}
