#include <iostream>
using namespace std;

long double fact(int n)  // 遞迴式函式
{
   if(n == 1)            // 在 n==1 時停止往下遞迴
     return 1;           // 傳回 1
   else
    return ( n * fact(n-1));   // 將參數減 1 再呼叫自己
}

int main()
{
   int x;
   while (true) {
     cout << "請輸入一小於170的整數(輸入0結束程式)：";
     cin >> x;
     if(x == 0) break;    // 輸入 0 時跳出迴圈、結束程式
     cout << x << "! = " << fact(x) << endl;
   }
}
