#include<iostream>
using namespace std;

int main()
{
  for (int i=1;i<=10;i++) { // 由 1 到 10 跑 10 次的迴圈
    if (i == 5)   // 迴圈執行到第 5 輪時, if 條件運算式成立
      continue;   // 跳出第 5 輪的迴圈, 繼續第 6 輪的迴圈
    cout << i << '_';
  }
}
