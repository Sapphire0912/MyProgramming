#include <iostream>
using namespace std;

int main()
{
  int    i;          // 宣告整數及變數
  double d;          // 宣告倍精度浮點數變數
  int    *iptr = &i; // 定義指標變數, 並將初始值設為 i 的位址
  double *dptr = &d; // 定義指標變數, 並將初始值設為 d 的位址

  cout << "iptr 的大小為：" << sizeof(iptr) << endl;
  cout << "iptr 存的值為：" << iptr << endl;

  cout << "dptr 的大小為：" << sizeof(dptr) << endl;
  cout << "dptr 存的值為：" << dptr << endl;
}
