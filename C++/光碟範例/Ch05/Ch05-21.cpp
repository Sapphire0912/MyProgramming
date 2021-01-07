#include<iostream>
using namespace std;

int main()
{
  while(true) {
    cout << "請輸入 1-170 間的整數(輸入 0 即結束程式)：";
    int num = 0;
    cin >> num;

    if (num == 0)
      break;          // 若使用者輸入 0, 就跳出迴圈

    cout << num << "! 等於 ";

    double fact;            // 用來儲存、計算階乘值的變數
    for(fact=1;num>0;num--) // 計算階乘的迴圈
      fact = fact * num;    // 每輪皆將 fact 乘上目前的 num

    cout << fact << "\n\n"; // 輸出計算所得的階乘值
  }
  cout << "謝謝您使用階乘計算程式。";
}
