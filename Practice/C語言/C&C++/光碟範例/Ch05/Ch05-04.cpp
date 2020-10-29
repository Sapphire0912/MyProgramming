#include<iostream>
using namespace std;

int main()
{
   float gasoline;
   cout << "請輸入目前所剩油量 (單位：公升)：";
   cin >> gasoline;

   if (gasoline >= 1)    // 第 1 個 if
     if (gasoline < 5)   // 第 2 個 if
      cout << "油量尚足, 但需注意油表！\n";

   cout << "祝您行車愉快。";
}
