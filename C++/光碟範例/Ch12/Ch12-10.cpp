#include<iostream>
using namespace std;

class Shape {
friend ostream& operator<<(ostream&, Shape&);
public:
  Shape (int i=0, int j=0) { x = i;     y = j; }
private:
  int x, y;         // 代表圖形的起點
};

ostream& operator<<(ostream& o, Shape& s)
{
   return o << '(' << s.x << ',' << s.y << ')';
}

class Circle : public Shape   { // 繼承 Shape 的特性
public:
  Circle(int i, int j, int radius): Shape(i,j)
  {                             // 呼叫父類別的建構函式
     r = radius;
  }
private:
  int r;  // 圓半徑
};

class Sphere : private Circle  { // 以 private 方式繼承
public:
  Sphere(int i, int j, int k, int radius): Circle(i,j,radius)
  { z = k; }
private:
  int z;     // Z 軸座標
};

int main()
{
  Circle disc(1,1,5);
  cout << disc;      // 將物件從輸出串流輸出
  Sphere baseball(0,0,0,10);
  cout << baseball;  // 將物件從輸出串流輸出
}
