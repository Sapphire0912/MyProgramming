#include <iostream>
using namespace std;

double fact(int n)    // 遞迴式函式
{
  if(n>170 || n<0)   // 計算的值太大或小於 0
    throw n;         // 將參數當成例外拋出
  else if (n==0)
    return 1;        // 0! 的值為 1

  double total = 1;
  for (int i=1; i<=n; i++)
    total *= i;
  return total;
}

int main()
{
  int x,y;
  cout << "本程式可計算 C(x,y) 的組合總數\n";

  while (true) {
    cout << "請輸入 x、y 的值 (輸入兩個 0 結束)：";
    cin >> x >> y;
    if(x == 0)
      break;     // 輸入 0 時跳出迴圈、結束程式

    try {
      cout << "C(" << x << ',' << y << ") = "
           << fact(x) / (fact(x-y)*fact(y)) << endl;
    }                // 『X 取 Y 的組合』之計算公式
    catch (int) {
      cerr << "輸入的數值太大或數值有誤，無法計算\n";
    }
  }
}
