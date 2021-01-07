#include<iostream>
using namespace std;

class Circle {
public:
  Circle(double,double,double);
  Circle(double,double,double,double);
  double area() { return 3.1415926 * r * r; }  // 計算圓面積
  double circum() { return 3.1415926 * 2 * r; }// 計算圓週長
private:
  double x,y;         // 圓心座標
  double r;           // 半徑
};

Circle::Circle(double x0,double y0,double r0 = 1)
{
  x = x0; y = y0; r = r0;
}

Circle::Circle(double x0,double y0,double x1, double y1)
{
  double w = min( (x1>x0)? (x1-x0):(x0-x1),    // 計算正方形邊長
                  (y1>y0)? (y1-y0):(y0-y1) );
  r = w/2;     // 半徑為寬或高的一半
  x = x0 + r;  // 算出圓心的 x 座標
  y = y0 + r;  // 算出圓心的 y 座標
}

int main()
{
  Circle c1(3,5),c2(10,10,30,30);
  cout << "c1 的面積為 " << c1.area() << endl;
  cout << "c2 的圓周長為 " << c2.circum() << endl;
}
