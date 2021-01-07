#include<iostream>
using namespace std;

int main()
{
  float gasoline;
  cout << "請輸入目前所剩油量 (單位：公升)：";
  cin >> gasoline;

  if (gasoline < 1)                    // 如果 gasoline 小於 1
    cout << "快沒油了, 該加油囉！\n";  // 就執行括號內的敘述

  cout << "祝您行車愉快。";
}
