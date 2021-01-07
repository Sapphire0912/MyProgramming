#include<iostream>
using namespace std;

int main()
{
  int i = 3;
  bool b = false;

  cout << boolalpha;  // 改用文字的方式輸出布林值
  cout << "i = " << i << "\tb =" << b << endl;
  cout << "i && b：" << (i && b) << endl;
  cout << "i || b：" << (i || b) << endl;
  cout << "i &&!b：" << (i &&!b) << endl;
  cout << "i ||!b：" << (i ||!b) << endl;
}
