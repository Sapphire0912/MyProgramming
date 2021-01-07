#include<iostream>
using namespace std;

class Time {
public:                 // 預設建構函式將時間設為 12 點整
  Time() { hour = 12; min = 0; sec = 0; };
  Time(int);            // 一個參數的建構函式
  Time(int,int,int);    // 三個參數的建構函式
  void show()
  {
    cout << hour << "點" << min << "分" << sec << "秒" << endl;
  }
private:
  int hour, min, sec;   // 代表時分秒的成員
};

Time::Time(int h)
{
  hour = (h>=0 && h<=23) ? h:12;     // 檢查 h 是否在 0 至 23 間
  min = 0; sec = 0;
}

Time::Time(int h,int m, int s)
{
  hour = (h>=0 && h<=23) ? h:12;     // 檢查 h 是否在 0 至 23 間
  min  = (m>=0 && m<=59) ? m:0;      // 檢查 m 是否在 0 至 59 間
  sec  = (s>=0 && s<=59) ? s:0;      // 檢查 s 是否在 0 至 59 間
}

int main()
{
  Time t1;           // 呼叫預設建構函式
  Time t2(9);        // 呼叫只有一個參數的建構函式
  Time t3(15,45,75); // 呼叫有三個參數的建構函式

  t1.show();
  t2.show();
  t3.show();
}
