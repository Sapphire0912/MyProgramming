#include<iostream>
using namespace std;

class Car {
public:
  static void setEff(double e) { eff = e;} // 設定靜態資料成員
  double getEff() { return eff; }
  static double GtoL(double G) { return G*3.78533; }
                // 將加侖換算為公升, 1加侖為 3.78533 公升
  static double LtoG(double L) { return L*0.26418; }
                // 將公升換算為加侖, 1公升為 0.26418 加侖
private:
  static double eff;    // 靜態資料成員
};

double Car::eff = 0;    // 定義靜態資料成員

int main()
{
  // 未建立物件也可呼叫靜態成員函式
  cout << "10加侖等於 " << Car::GtoL(10) << " 公升" << endl;
                           // 用物件呼叫成員函式
  cout << "10公升等於 " << Car::LtoG(10) << " 加侖" << endl;
                           // 用類別呼叫成員函式

  Car super;           // 宣告物件
  super.setEff(30);    // 用物件也可呼叫靜態成員函式

  cout << "超級省油車1公升跑 " << super.getEff()
       << " 公里" << endl;
}
