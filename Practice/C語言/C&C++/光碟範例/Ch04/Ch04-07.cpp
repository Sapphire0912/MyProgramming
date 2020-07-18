#include<iostream>
using namespace std;

int main()
{
  int i = 3, j = 3;

  cout << boolalpha;  // 改用文字的方式輸出布林值

  cout << "(i == j) ：" << (i == j) << endl;
  cout << "(i > j)  ："  << (i > j) << endl;
  cout << "(++i > j)："<< (++i > j) << endl;
  cout << "(j-- < 3)："<< (j-- < 3) << endl;
  cout << "(i != j) ：" << (i != j) << endl;
}
