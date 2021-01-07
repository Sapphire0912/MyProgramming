#include<iostream>
using namespace std;

int main()
{
   float height;
   cout << "請輸入身高 (單位：公分)：";
   cin >> height;

   if (height > 110)
     cout << "身高超過標準，請購票上車！\n";
   else                 // 條件式不成立時才會執行此部份
     cout << "身高低於標準，可免購票！\n";

   cout << "祝旅途愉快。";
}
