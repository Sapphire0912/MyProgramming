#include<iostream>
using namespace std;

class Time {
public:                 // 建構函式只輸出一段訊息
  Time() { cout << "...正在執行 Time 的建構函式" << endl; };
private:
  int hour, min, sec;   // 代表時分秒的成員
};

class Clock {
public:
  Clock() { cout << "...正在執行 Clock 的建構函式" << endl; };
private:
  Time clock_time;     // 時鐘時間
  Time alarm_time;     // 鬧鐘時間
};

int main()
{
  Clock old_clock;   // 建立 Clock 物件
}
