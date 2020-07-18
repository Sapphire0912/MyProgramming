#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  double a, b;

  cout << "本程式可計算直角三角形的斜邊長" << endl;
  cout << "請輸入直角三角型第1個短邊的邊長：";
  cin >> a;
  cout << "請輸入直角三角型第2個短邊的邊長：";
  cin >> b;
  cout << "斜邊長為：" << sqrt(a*a + b*b);
}
