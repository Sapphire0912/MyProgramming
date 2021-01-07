#include<iostream>
using namespace std;

int main()
{
  int range;
  cout << "請輸入要尋找的範圍：";
  cin >> range;

  int count = 0;             // 用來計算共有幾個質數

  for (int i=2;i<=range;i++) {
    bool isPrime = true;     // 表示目前的 i 是否為質數的布林值

    for (int j=2;j<i;j++)    // 做除法運算的內迴圈
      if ((i%j) == 0) {      // 餘數為 0 表示可以整除,
        isPrime = false;     // 所以不是質數,
        break;               // 也不用繼續除了
      }

    if (isPrime) {           // 若是質數, 即輸出該數值
      cout << i << '\t';
      count++;
      if ((count%5) == 0)   // 設定每輸出五個質數就換行
        cout << endl;
    }
  }

  cout << "\n小於等於 "  << range << " 的質數共有 "
       << count << " 個";
}
