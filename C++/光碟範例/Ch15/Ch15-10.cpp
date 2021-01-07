#include <iostream>
#include "Ch15-10.h"

void main()
{
  Stack st;     // 定義堆疊物件

  try {
    for (int i=0; i<=20; i++)  // 用迴圈放入 21 筆資料
      st.push(i);
  }
  catch (StackFull) {
    cerr << "操作錯誤, 堆疊已滿\n";
  }

  try {
    for (int i=0; i<=20; i++)  // 用迴圈取出 21 筆資料
      cout << st.pop() << '\t';
  }
  catch (StackEmpty) {
    cerr << "操作錯誤, 堆疊已清空\n";
  }
}
