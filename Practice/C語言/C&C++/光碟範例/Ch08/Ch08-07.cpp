#include<iostream>
using namespace std;

class Str {           // 陽春的字串類別
public:
  void show() { cout << str; }
  void set(char * ptr) { str = ptr; }
  void showthis() { cout << this; }  // 輸出 this 指標
private:
  char * str;       // 指向字串的指標
};

int main()
{
  Str hello, world;
  hello.set("Hello");  world.set("World!");
  cout << "hello 物件的位址：" << &hello << endl;
  cout << "world 物件的位址：";
  world.showthis();
}
