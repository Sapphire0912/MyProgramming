#include<iostream>
using namespace std;

int main()
{
  int choice;
  cout << "我們有四種餐, 請選擇：\n";
  cout << "1.炸雞餐 2.漢堡餐 3.起司堡餐 4.薯條餐：";
  cin >> choice;

  switch (choice) {
    case 1: // 炸雞餐價錢 109 元
      cout << "您點的餐點價錢為 109 元";
      break;
    case 2: // 漢堡餐和起司堡餐同價
    case 3: // 起司堡餐價錢為 99 元
      cout << "您點的餐點價錢為 99 元";
      break;
    case 4: // 薯條餐價錢為 69 元
      cout << "您點的餐點價錢為 69 元";
      break;
  }
}
