#include <iostream>
#include "Ch16-07.h"

void main()
{
   Stack<int> st1;  // 定義一個整數堆疊
   Stack<char,10> st2; // 定義一個字元堆疊
   st1.init();
   st2.init();

   // 將資料存入第一個堆疊中
   st1.push(1); st1.push(2); st1.push(3);

   // 將資料存入第二個堆疊中
   st2.push('a'); st2.push('b'); st2.push('c');

   cout << st1.pop();
   cout << st2.pop();
   cout << st1.pop();
   cout << st2.pop();
   cout << st1.pop();
   cout << st2.pop();    st2.pop(); // 故意多 pop 一次
}