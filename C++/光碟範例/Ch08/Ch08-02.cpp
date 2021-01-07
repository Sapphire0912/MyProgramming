#include<iostream>
using namespace std;

class Car {   // 定義類別
public:       // 成員函式設為公開
  void init(double,double);        // 初始化函式
  double getEff()   { return eff;} // 傳回燃油效率
  double checkGas() { return gas;} // 檢查油量, 傳回剩餘油量
  double go(double);  // 行走參數指定里程, 傳回實際行走里程
private:      // 讓資料成員為私有
  double gas; // 載油量
  double eff; // 每公升可行駛公里數
};

double Car::go(double kilo)
{
  if (gas >= (kilo/eff)) { // 若油量夠
    gas -= kilo/eff;       // 減掉所耗掉的油量
    cout << "油箱還有 " << checkGas() << " 公升油" << endl;
    if (gas == 0)             // 油用完了
      cout << "沒油了！";
  } else {
    cout << "油量不夠，目前的油只夠跑 "
         << (kilo = gas * eff) << " 公里";
    gas = 0;
  }
  return kilo;
}

void Car::init(double G,double E)
{
  gas = G;  // 初始化油量
  eff= E;   // 初始化燃油效率
}

int main()
{
  Car super;            // 宣告物件
  super.init(20,30);    // 初始化物件
  cout << "超級省油車1公升跑 " << super.getEff()
       << " 公里" << endl;
  cout << "現在油箱有 " << super.checkGas() << " 公升油" << endl;

  while (super.checkGas() > 0) {
    double kilo;
    cout << "現在要開幾公里：";
    cin >> kilo;
    super.go(kilo);     // 行走指定里程
  }
}
