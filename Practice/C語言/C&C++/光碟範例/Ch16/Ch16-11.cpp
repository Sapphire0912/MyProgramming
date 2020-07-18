#include <iostream>
#include <stack>
using namespace std;

int main()
{
   stack<int> st1;  // 定義一個整數堆疊
   stack<char> st2; // 定義一個字元堆疊

   // 將資料存入第一個堆疊中
   st1.push(1); st1.push(2); st1.push(3);

   // 將資料存入第二個堆疊中
   st2.push('a'); st2.push('b'); st2.push('c');

   cout << st1.top();st1.pop();
   cout << st2.top();st2.pop();
   cout << st1.top();st1.pop();
   cout << st2.top();st2.pop();
   cout << st1.top();st1.pop();
   cout << st2.top();st2.pop();
}
