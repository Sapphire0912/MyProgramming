#include <iostream>
using namespace std;

inline double FtoC (double f)   // 定義為行內函式
{
  return (f - 32) * 5 / 9;
}

int main()
{
  double F;
  cout << "請輸入華氏的溫度：";
  cin >> F;

  cout << "換算成攝氏溫度為 " << FtoC(F) << " 度";
}
