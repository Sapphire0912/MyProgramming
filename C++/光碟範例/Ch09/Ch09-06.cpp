#include<iostream>
using namespace std;

class Time {
public:
  Time(int,int,int);    // Τ篶ㄧΑ
  void show()
  {
    cout << hour << "翴" << min << "だ" << sec << "" << endl;
  }
private:
  int hour, min, sec;   // だΘ
};

Time::Time(int h =12, int m=1, int s=1)
{
  hour = (h>=0 && h<=23) ? h:12;     // 浪琩 h 琌 0  23 丁
  min  = (m>=0 && m<=59) ? m:0;      // 浪琩 m 琌 0  59 丁
  sec  = (s>=0 && s<=59) ? s:0;      // 浪琩 s 琌 0  59 丁
}

int main()
{
  Time t1;           // ぃ把计
  Time t2(10);       // 把计
  Time t3(8,24);     // 把计
  Time t4(10,20,30); // 把计

  t1.show();   t2.show();
  t3.show();   t4.show();
}
