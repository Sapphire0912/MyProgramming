#include<iostream>
using namespace std;

class Time {
  friend Time& operator++(Time&);
  friend Time& operator--(Time&);
public:
  Time(int,int,int);    // 只有一個建構函式
  void show()
  {
    cout << hour << "點" << min << "分" << sec << "秒" << endl;
  }
private:
  int hour, min, sec;   // 代表時分秒的成員
};

Time::Time(int h =12 ,int m=0 , int s=0)
{
  hour = (h>=0 && h<=23) ? h:12;     // 檢查 h 是否在 0 至 23 間
  min  = (m>=0 && m<=59) ? m:0;      // 檢查 m 是否在 0 至 59 間
  sec  = (s>=0 && s<=59) ? s:0;      // 檢查 s 是否在 0 至 59 間
}

Time& operator++(Time& t)            // 夥伴函式
{
  if (++t.sec == 60) {
    t.sec = 0;
    if (++t.min == 60) {
       t.min = 0;
       if (++t.hour == 24)
         t.hour = 0;
    }
  }
  return t;                          // 傳回物件
}

Time& operator--(Time& t)            // 夥伴函式
{
  if (--t.sec == -1) {
    t.sec = 59;
    if (--t.min == -1) {
       t.min = 59;
       if (--t.hour == -1)
         t.hour = 23;
    }
  }
  return t;                          // 傳回物件
}

int main()
{
  Time t1(9,59,59);
  Time t2(10);

  (++t1).show();
  (--t2).show();
}
