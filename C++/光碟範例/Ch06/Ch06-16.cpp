#include <iostream>
using namespace std;

void volume (double r) // 計算球體體積
{
  cout << "半徑 " << r << " 的球體體積為 "
       << 4 / 3 * 3.14159 * r * r * r << endl;
}
                         // 計算長方體體積
void volume (double l, double w, double h)
{
  cout << "長 " << l << " 寬 " << w << " 高 " << h
       << " 的長方體體積為 "<< l * w * h << endl;
}

int main()
{
  volume(15);
  volume(5,15,25);
}
