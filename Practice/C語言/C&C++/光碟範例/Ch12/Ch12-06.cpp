#include<iostream>
using namespace std;

class Shape {
public:
  Shape (int i=0, int j=0) { x = i;     y = j; }
  double getX() { return x;}
  double getY() { return y;}
protected:
  double x, y;         // 代表圖形的起點
};

class Rectangle : public Shape   { // 繼承 Shape
public:
  Rectangle(int i, int j, int k, int l):Shape(i,j)
  { x = k; y = l; }
  double getX() { return x;}  // 與父類別的
  double getY() { return y;}  // 成員函式同名
  double area();              // 計算面積的函式
private:
  double x,y;          // 與父類別的資料成員同名
};

double Rectangle::area()
{
  return (x - Shape::getX()) * (y - Shape::getY());
}          // 以範圍解析運算子標明要呼叫的版本

int main()
{
  Rectangle r(0,0,3,5);
  cout << "矩形的面積為 " << r.area();
}
