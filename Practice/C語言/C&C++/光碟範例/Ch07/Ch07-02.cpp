#include <iostream>
using namespace std;

int main()
{
  int iArray[] = {1,2,3,4,5};  // 未指定陣列大小
  int nArray[5] = {6,7,8};     // 未設定全部元素的初始值

  cout << "iArray 陣列的大小為 " << sizeof(iArray)
       << " 個位元組" << endl;
  cout << "nArray 陣列的大小為 " << sizeof(nArray)
       << " 個位元組" << endl;

  for(int i=0;i<5;i++) {  // 用迴圈輸出各元素值
    cout << "iArray[" << i << "] =" << iArray[i] << '\t'   
         << "nArray[" << i << "] =" << nArray[i] << endl;
  }
}
