#include<iostream>
using namespace std;

class Car {
public:
  double getEff()       { return eff;} // 傳回燃油效率
  void setEff(double d) { eff = d;}    // 設定燃油效率
private:
  static double eff;       // 靜態成員
};

double Car::eff = 30.0;  // 定義及初始化靜態資料成員的值

int main()
{
  Car *One = new Car;
  One->setEff(8);    // 設定一號車1公升油可跑8公里
  cout << "一號車1公升油可跑 " << One->getEff()
       << " 公里" << endl;
}
