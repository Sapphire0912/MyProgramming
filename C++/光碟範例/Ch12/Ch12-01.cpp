#include<iostream>
using namespace std;

class Shape {
public:
  double x, y;         // 代表圖形的起點
};

class Rectangle : public Shape   { // 繼承自 Shape 類別
  double x2,y2;        // 代表矩形右下角成員
};

class Circle : public Shape   {    // 繼承自 Shape 類別
  double r;            // 代表圓半徑
};

int main()
{
  Shape s;
  Rectangle r;
  Circle c;
  cout << "s 的大小：" << sizeof(s) << endl;
  cout << "r 的大小：" << sizeof(r) << endl;
  cout << "c 的大小：" << sizeof(c) << endl;
}
