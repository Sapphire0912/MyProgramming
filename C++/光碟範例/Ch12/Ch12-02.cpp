#include<iostream>
using namespace std;

class Shape {
public:
  Shape (int i=0, int j=0)
  {
     x = i;     y = j;
     cout << "正在執行 Shape 的建構函式" << endl;
  }
private:
  double x, y;         // 代表圖形的起點
};

class Circle : public Shape   { // 繼承 Shape 的特性
public:
  Circle() { cout << "正在執行 Circle 的建構函式" <<endl; }
private:
  double r;            // 代表圓半徑
};

int main()
{
  Circle c;  // 建立 Circle 物件
}
