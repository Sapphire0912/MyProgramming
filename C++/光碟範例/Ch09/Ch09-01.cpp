#include<iostream>
using namespace std;

class Time {
public:                 // 建構函式只輸出一段訊息
  Time() { cout << "...正在執行 Time 的建構函式" << endl; };
private:
  int hour, min, sec;   // 代表時分秒的成員
};

void main()
{
  cout << "宣告 t1、t2 物件" << endl;
  Time t1, t2;
  cout << "宣告物件指標 t3" << endl;
  Time* t3;  // 編譯器會對這行敘述發出警告, 先不予理會
  cout << "定義物件指標 t4" << endl;
  Time* t4 = new Time;
}
