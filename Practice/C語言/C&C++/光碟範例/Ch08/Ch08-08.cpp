#include<iostream>
using namespace std;

class Time {
public:
  void set(int, int, int);
  void copy(Time source) { *this = source; } // 複製資料成員
  void show() { cout << hour << ':' << min << ':' << sec; }
private:
  int hour, min, sec;   // 代表時分秒的成員
};

void Time::set(int hour, int min, int sec)   // 參數名稱與
{                                            // 資料成員相同
  this->hour = hour;    // 將參數 hour 的值指定給資料成員 hour
  this->min  = min;     // 將參數 min  的值指定給資料成員 min
  this->sec  = sec;     // 將參數 sec  的值指定給資料成員 sec
}

void main()
{
   Time t1, t2;
   t1.set(12,15,30);
   t2.copy(t1);  // 將 t1 的內容複製到 t2
   t2.show();
}
