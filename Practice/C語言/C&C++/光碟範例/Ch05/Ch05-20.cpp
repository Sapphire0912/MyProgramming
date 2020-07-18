#include<iostream>
using namespace std;

int main()
{
  float i,j,k;       // 用來儲存 3 邊的邊長

  cout << "請依序輸入三角形的三邊長：\n";
  cout << "邊長 1 →";
  cin >> i;          // 輸入第 1 邊邊長
  cout << "邊長 2 →";
  cin >> j;          // 輸入第 2 邊邊長
  cout << "邊長 3 →";
  cin >> k;          // 輸入第 3 邊邊長

  if ((i+j) > k)     // 判斷第 1, 2 邊的和是否大於第 3 邊
    if ((i+k) > j)   // 判斷第 1, 3 邊的和是否大於第 2 邊
      if ((j+k) > i) // 判斷第 2, 3 邊的和是否大於第 1 邊
        cout << "可以為三角形的三邊長。";
      else
        cout << "第 2、3 邊的和小於或等於第 1 邊";
    else
      cout << "第 1、3 邊的和小於或等於第 2 邊";
  else
    cout << "第 1、2 邊的和小於或等於第 3 邊";
}
