#include <iostream>
using namespace std;

int main()
{
  int iArray[3][4] = {1,2,3,4,5,6};

  cout << "iArray 陣列的大小為 " << sizeof(iArray)
       << " 個位元組" << endl;

  for(int i=0;i<3;i++) {  // 用巢狀迴圈遊歷所有的元素
    for(int j=0;j<4;j++)
      cout << "iArray[" << i << "][" << j << "]= "
           << iArray[i][j] << '\t';

    cout << endl;        // 每輸出完一列元素就換行
  }
}
