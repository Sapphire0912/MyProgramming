#include<iostream>
using namespace std;

int main()
{
  const double PI = 3.1415926;  // 定義唯讀變數
  double area;

  // 用唯讀變數計算圓面積
  area = 5 * 5 * PI;
  cout << "半徑 5 的圓面積等於 " << area << endl;

  area = 15 * 15 * PI;
  cout << "半徑 15 的圓面積等於 " << area << endl;
}
