#include<iostream>
using namespace std;

int main()
{
  for (int x=1; x < 10; x++) {  // 外迴圈, x 的值由 1 到 9
    for (int y=1; y < 10; y++)  // 內迴圈, y 的值由 1 到 9
      cout << x << '*' << y << '=' << x*y << '\t';
    cout << endl;               // 外迴圈每執行一次就換行
  }
}
