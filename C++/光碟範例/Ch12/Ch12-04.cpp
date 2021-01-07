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

class Circle : public Shape   { // 繼承 Shape 的特性
  friend ostream& operator<<(ostream& o, Circle& c);
public:
  Circle(int i, int j, int radius)
  { x = i; y = j;  r = radius; } // 直接存取 protected 資料成員
private:
  double r;            // 代表圓半徑
};

ostream& operator<<(ostream& o, Circle& c) // 輸出圓點座標及半徑
{                    // 可直接存取 protected 資料成員
  return o << '(' << c.x << ',' << c.y << ')' << endl
           << "r = " << c.r;
}

int main()
{
  Circle c(1,3,5);  // 建立 Circle 物件
  cout << c;
}
