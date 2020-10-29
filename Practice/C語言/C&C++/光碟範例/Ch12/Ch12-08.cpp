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
  return o << '(' << c.getX() << ',' << c.getY() << ')' << '\t'
           << "r = " << c.r << endl;
}

int main()
{
  Circle small(1,2,1);  // 建立 Circle 物件
  Circle c = small;     // 將呼叫預設的複製建構函式
  cout << c;
  Circle big(3,3,100);
  c = big;              // 將呼叫預設的 operator= 運算子
  cout << c;
}
