#include <iostream>
using namespace std;

int main()
{
  int age=18;
  int &old=age;  // 定義參考型別變數

  cout << "age的值：" << age << "\told的值：" << old << endl;
  cout << endl << "請輸入 age 的新數值：";
  cin >> age;;
  cout << "age的值：" << age << "\told的值：" << old << endl;
  cout << endl << "請輸入 old 的新數值：";
  cin >> old;;
  cout << "age的值：" << age << "\told的值：" << old << endl;
}
