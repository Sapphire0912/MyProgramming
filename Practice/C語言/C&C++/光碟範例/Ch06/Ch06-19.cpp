#include <iostream>
#include <cmath>
using namespace std;

inline double root(double x, int n) { return pow(x,1.0/n); }

int main()
{
  int n;
  double x;
  while (true)
  {
    cout << "請輸入要求 n 次方根的正實數(輸入0則結束程式)：";
    cin >> x;
    cout << "要求幾次方根(限輸入整數)：";
    cin >> n;

    if(x == 0 || n==0)    // 輸入 0 時跳出迴圈、結束程式
      break;
    else if (x < 0)       // 若 x 為負值, 將其變成正值
      x *= -1;            // 也可呼叫 <cmath> 的絕對值函式 abs()
    cout << x << " 的 " << n << " 次方根為 " << root(x,n) << endl;
  }
}
