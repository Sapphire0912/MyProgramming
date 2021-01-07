#include <iostream>
#include <exception>
#define MaxSize 20
using namespace std;

class StackFull : public exception {};  // 自訂的例外類別
class StackEmpty: public exception {};

class Stack {
public:
  Stack() { sp = 0; }   // 建構函式, 將 sp 設為 0 表示堆疊是空的
  void push(int data);  // 宣告存入一個整數的函式
  int pop();            // 宣告取出一個整數的函式
private:
  int sp;               // 用來記錄目前堆疊中已存幾筆資料
  int buffer[MaxSize];  // 代表堆疊的陣列
};

void Stack::push(int data)   // 將一個整數『堆』入堆疊
{
   if(sp == MaxSize)         // 若已達最大值, 則不能再放資料進來
     throw StackFull();      // 拋出自訂的 StackFull 例外
   else
     buffer[sp++] = data;    // 將資料存入 sp 所指元素, 並將 sp 加 1
}                            // 表示所存的資料多了一筆

int Stack::pop()             // 從堆疊中取出一個整數
{
   if(sp == 0)               // 若已經到底了, 表示堆疊中應無資料
     throw StackEmpty();     // 拋出自訂的 StackEmpty 例外
   return buffer[--sp];      // 傳回 sp 所指的元素, 並將 sp 減 1
}                            // 表示所存的資料少了一筆
