#include <iostream>
using namespace std;

int main()
{
  int iArray[5];          // 宣告陣列

  for(int i=0;i<5;i++)    // 用迴圈設定各元素值
    iArray[i] = i * 5;

  cout << "iArray 陣列的大小為 " << sizeof(iArray)
       << " 個位元組" << endl;
  for(int i=0;i<5;i++)    // 用迴圈輸出各元素值
    cout << "iArray[" << i << "] =" << iArray[i] << endl;
}
