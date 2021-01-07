#include <iostream>
#include "Ch08-12.h"

int main()
{
   Stack st1, st2;    // 定義二個堆疊物件
   st1.init();
   st2.init();

   // 將資料存入第一個堆疊中
   st1.push(1); st1.push(2); st1.push(3);

   // 將資料存入第二個堆疊中
   st2.push(7); st2.push(8); st2.push(9);

   cout << st1.pop();
   cout << st2.pop();
   cout << st1.pop();
   cout << st2.pop();
   cout << st1.pop();
   cout << st2.pop();    st2.pop(); // 故意多 pop 一次
}
