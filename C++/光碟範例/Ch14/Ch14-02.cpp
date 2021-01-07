#include<iostream>
using namespace std;

int main()
{
  int i;
  cerr << "轉向測試, 請輸入一個數字：";
  cin >> i;
  cout << "輸入的數字是" << i << endl;  // 標準輸出可轉向
  clog << "程式結束。";
}
