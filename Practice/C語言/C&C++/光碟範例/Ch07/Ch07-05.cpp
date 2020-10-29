#include <iostream>
using namespace std;

int main()
{
  char name1[]="John Smith";  // 以字串為初始值
  char name2[]={'M','a','r','y',' ','W','h','i','t','e'};
                              // 設定個別字元為初始值
  cout << "name1[]大小為：" << sizeof(name1) << endl;
  cout << "name2[]大小為：" << sizeof(name2) << endl;

  cout << "name1[]：" << name1 << endl;
  cout << "name2[]：" << name2 << endl;
}
