#include<iostream>
using namespace std;

int main()
{
  int i = 3, j = 0;

  cout << boolalpha; // 改用文字的方式輸出布林值

  cout << "i = " << i << "\tj =" << j << endl;
  cout << "i || (j++)：" << (i || (j++)) << endl;
  cout << "i = " << i << "\tj =" << j << endl;

  cout << "j && (++i)：" << (j && (++i)) << endl;
  cout << "i = " << i << "\tj =" << j << endl;
}
