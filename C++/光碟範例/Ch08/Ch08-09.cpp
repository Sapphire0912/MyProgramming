#include<iostream>
using namespace std;

class Time {
public:
  Time& set(int, int, int);   // 宣告為傳回 Time 參考型別
  void copy(Time source) { *this = source; }   // 複製資料成員
  void show() { cout << hour << ':' << min << ':' << sec; }
private:
  int hour, min, sec;   // 代表時分秒的成員
};

Time& Time::set(int h, int m, int s)
{
   hour = h; min  = m; sec  = s;
   return *this;     // 傳回原呼叫者物件
}

void main()
{
   Time t;
   t.set(13,42,56).show();
}
