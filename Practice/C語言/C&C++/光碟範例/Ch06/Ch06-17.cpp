#include <iostream>

int main()
{
   void func();   // 宣告函式
   func();        // 呼叫函式
}

void  func()      // 遞迴函式
{
   std::cout << "This is a endless program\n";
   func();    // 呼叫自己
}
