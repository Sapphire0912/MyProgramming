#include<iostream>
using namespace std;

int main()
{
  int season;
  cout << "請選擇季節：1.春 2.夏 3.秋 4.冬：";
  cin >> season;

  switch (season)
  {
    case 1:  // 當 season 的數值為 1
      cout << "請穿著長袖出門";
      break; // 結束此 case
    case 2:  // 當 season 的數值為 2
      cout << "請穿著短袖出門";
      break; // 結束此 case
    case 3:  // 當 season 的數值為 3
      cout << "請加件長袖輕薄外套出門";
      break; // 結束此 case
    case 4:  // 當 season 的數值為 4
      cout << "請穿著毛衣或大衣出門";
      break; // 結束此 case
  }
}
