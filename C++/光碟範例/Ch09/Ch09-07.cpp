#include "Ch09-07.h"         // 含括自訂的含括檔

int main()
{
  Str hello("Hello World!"); // 呼叫有參數的版本
  Str world = hello;         // 用舊物件初始化新物件
  hello.show();
  world.show();
}
