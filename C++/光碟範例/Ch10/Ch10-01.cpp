#include "Ch10-01.h"    // 含括類別定義

int main()
{
  Str array[2] = {0, Str("Apple Pie")}; // 含 2 個字串物件的陣列

  for(int i=0;i<2;i++)  // 用迴圈輸出各元素物件的字串
    cout << "array[" << i << "] 的長度"
         << (!array[i] ? "為 0" : "不為 0") << endl;
}
