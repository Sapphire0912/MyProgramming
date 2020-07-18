#include<iostream>
using namespace std;

int main()
{
  enum fruit_tea { apple, banana, orange };
  fruit_tea taste;   // taste 是 fruit_tea 型別的物件

  taste = apple;     // 需用列舉成員來設定其值
  cout << "taste = " << taste << endl;

  taste = orange;
  cout << "taste = " << taste << endl;
}
