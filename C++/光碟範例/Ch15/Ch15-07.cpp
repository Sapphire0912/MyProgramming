#include<iostream>
using namespace std;

void divide(int i, int j)  // 除法運算的函式
{
  if (j == 0)       // 若除數為零
    throw j;        // 即拋出例外
  else
    cout << i << '/' << j << " = " << i/j << "..." << i%j;
}

int main()                 // 測試用的主程式
{
  int i,j;
  cout << "本程式會計算除法運算中的商及餘數, "
       << "請依序輸入被除數與除數：";
  cin >> i >> j;

  try {
    divide (i,j);          // 呼叫除法函式
  }
  catch (int) {            // 補捉整數型別的例外
    cerr << "\n...發生除以零的例外...";
  }
}
