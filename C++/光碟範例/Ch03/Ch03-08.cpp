#include<iostream>
using namespace std;

int main()
{
  bool test1,test2;
  test1 = true;
  test2 = 0;    // 相當於設為 false
  cout << "test1 = " << test1 << endl
       << "test2 = " << test2 << endl;

  // 改用文字的方式輸出布林值
  cout << boolalpha;
  cout << "test1 = " << test1 << endl
       << "test2 = " << test2 << endl;
}
