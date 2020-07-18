#include <iostream>
using namespace std;
#define XX (c*e- f*b)/(a*e- d*b)  // 定義解 x 的巨集
#define YY (a*f- d*c)/(a*e- d*b)  // 定義解 y 的巨集

int main()
{
  float a,b,c,d,e,f;              // 二元一次方程式的係數
  char go = 'y';

  cout << "解聯立方程式" << endl
       << "ax + by = c" << endl
       << "dx + ey = f" << endl;

  while (go == 'y' || go =='Y') {
    cout << "請輸入a的值：";  cin >> a;
    cout << "請輸入b的值：";  cin >> b;
    cout << "請輸入c的值：";  cin >> c;
    cout << "請輸入d的值：";  cin >> d;
    cout << "請輸入e的值：";  cin >> e;
    cout << "請輸入f的值：";  cin >> f;

    if ((a*e- d*b)== 0)      // 避免分母為 0
      continue;

    cout << a << "x + " << b << "y = " << c << endl;
    cout << d << "x + " << e << "y = " << f << endl;
    cout << "的解為 x = " << XX << endl
         << "       y = " << YY << endl;

    cout << "還要再算嗎？(y/n)：";
    cin >> go;
  }
}
