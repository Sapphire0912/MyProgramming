#include <iostream>
#include <cstdlib>
using namespace std;

long double fact(int n) // 遞迴式函式
{
   if(n == 1)           // 在 n==1 時停止往下遞迴
     return 1;          // 傳回 1
   else
    return ( n * fact(n-1));   // 將參數減 1 再呼叫自己
}

int main(int argc, char *argv[])
{
   if (argc > 1)        // 若有命令列參數
     for(int i=1;i<argc;i++) {
       int f = atoi(argv[i]);
       cout << f << "! = " << fact(f) << endl;
     }
   else                 // 若沒有加參數就輸出使用說明
     cout << "用法：\"程式名稱 數字\"" << endl;
}
