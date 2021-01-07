#include<iostream>
using namespace std;

int main()
{
   float height;
   cout << "請輸入身高 (單位：公分)：";
   cin >> height;

   if (height < 110)
     cout << "身高低於標準，可免購票！\n";
   else if (height < 140) // 身高在 110 及 140 間的狀況
     cout << "身高超過 110，請買半票！\n";
   else                   // 身高超過 140 的狀況
     cout << "身高超過 140，請買全票！\n";

   cout << "祝旅途愉快。";
}
