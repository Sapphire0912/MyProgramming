#include "Ch09-09.h"    // 直接用前一範例的含括檔

int main()
{
  Str array[4] = {10, Str("Apple "), "Pie"};

  cout << "Str  物件佔用的位元組：" << sizeof(Str)   << endl
       << "array陣列佔用的位元組：" << sizeof(array) << endl;
  for(int i=0;i<4;i++)  // 用迴圈輸出各元素物件的字串
    array[i].show();
}
