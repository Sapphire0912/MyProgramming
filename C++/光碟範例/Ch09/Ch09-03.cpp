#include<iostream>
using namespace std;

class Time {
public:                 // 預設建構函式將時間設為 12 點整
  Time() { hour = 12; min = 0; sec = 0; };
  void show()
  {
    cout << hour << "點" << min << "分" << sec << "秒" << endl;
  }
private:
  int hour, min, sec;   // 代表時分秒的成員
};

void main()
{
  Time t[3];             // 建立含 3 個 Time 物件的陣列
  for (int i =0;i<3;i++) // 用迴圈顯示每個物件的時間
    t[i].show();
}
