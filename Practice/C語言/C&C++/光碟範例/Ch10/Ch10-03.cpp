#include<iostream>
using namespace std;

class Time {
public:
  Time(int,int,int);    // 只有一個建構函式
  void show()
  {
    cout << hour << "點" << min << "分" << sec << "秒" << endl;
  }
  Time& operator++();
  Time& operator--();
private:
  int hour, min, sec;   // 代表時分秒的成員
};

Time::Time(int h =12 ,int m=0 , int s=0)
{
  hour = (h>=0 && h<=23) ? h:12;     // 檢查 h 是否在 0 至 23 間
  min  = (m>=0 && m<=59) ? m:0;      // 檢查 m 是否在 0 至 59 間
  sec  = (s>=0 && s<=59) ? s:0;      // 檢查 s 是否在 0 至 59 間
}

Time& Time::operator++()
{
  if (++sec == 60) {         // 若變成 60 秒
    sec = 0;                 // 則設為 0 秒並加 1 分
    if (++min == 60) {       // 若變成 60 分
       min = 0;              // 則設為 0 分並加 1 小時
       if (++hour == 24)     // 若變成 24 時
         hour = 0;           // 則設為 0 時
    }
  }
  return *this;
}

Time& Time::operator--()
{
  if (--sec == -1) {         // 若變成 -1 秒
    sec = 59;                // 則設為 59 秒並減 1 分
    if (--min == -1) {       // 若變成 -1 分
       min = 59;             // 則設為 59 分並減 1 小時
       if (--hour == -1)     // 若變成 -1 時
         hour = 23;          // 則設為 23 時
    }
  }
  return *this;
}

int main()
{
  Time t1(9,59,59);
  Time t2(10);

  (++t1).show();
  (--t2).show();
}
