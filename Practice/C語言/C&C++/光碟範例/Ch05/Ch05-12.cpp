#include<iostream>
using namespace std;

int main()
{
  int sum = 0;       // 儲存總和的變數

  for (int i=1; i<=100; i++) {
    sum += i;        // 將 sum 加上目前的 i 值
    cout << "1 加到 " << i << " 的總和為 " << sum << endl;
  }
}
