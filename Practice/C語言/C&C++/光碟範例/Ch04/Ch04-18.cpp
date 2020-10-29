#include <iostream>
using namespace std;

int main()
{
  int money;
  int ten,five,one;

  cout << "請輸入您的換幣金額：";
  cin >> money;
  ten = money / 10;     // 計算拾圓硬幣的個數
  five = (money%10)/5;  // 計算伍圓硬幣的個數
  one = (money%10)%5;   // 計算壹圓硬幣的個數
  cout << money << " 元共可兌換零錢：\n"
       << " 拾圓 " << ten << " 個\n"
       << " 伍圓 " << five << " 個\n"
       << " 壹圓 " << one << " 個\n";
}
