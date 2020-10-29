#include<iostream>
using namespace std;

class Vehicle {        // 交通工具類別
public:
  Vehicle(double p = 0)
  {
    cout << "Vehicle 物件建構中" << endl;
    speed = p;
  }
protected:
  double speed;        // 速度
};

class ExerciseTool {   // 運動器材類別
public:
  ExerciseTool(double w = 100)
  {
    cout << "ExerciseTool 物件建構中" << endl;
    weight = w;
  }
protected:
  double weight;       // 重量
};

class Bicycle: public Vehicle, public ExerciseTool { // 多重繼承
public:
  Bicycle(bool b = true) { discBreak = b; }
private:
  bool discBreak;      // 是否使用碟剎
};

int main()
{
  Bicycle bike;        // 宣告自行車物件
}
