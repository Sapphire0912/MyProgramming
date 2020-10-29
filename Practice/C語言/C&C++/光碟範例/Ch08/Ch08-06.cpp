#include<iostream>
#include<cstring>
using namespace std;

class Str {           // 陽春的字串類別
public:
  void show() { cout << data;}
  void set(char * ptr) { data = ptr; }
  void set()               // 多載函式
  {
    data = new char[40];   // 配置新的記憶體空間
    strcpy(data,"Empty!"); // 將 "Empty!" 複製到新的空間
  }
private:
  char * data;             // 指向字串的指標
};

int main()
{
  Str hello, world;
  hello.set("Hello World!");  // 呼叫有參數的版本
  world.set();                // 呼叫無參數的版本
  hello.show(); world.show();
}
