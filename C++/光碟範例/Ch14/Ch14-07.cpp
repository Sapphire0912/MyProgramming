#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
  cout.fill('*');   // 填充字元設為 '*'
  cout << setw(8) << -1000    << endl;
  cout << setw(8) << internal << -1000 << endl;
  cout << setw(8) << left     << -1000 << endl;

  cout.width(9);    // 設定寬度為 9 個字元
  cout << setfill('_') << "Good" << endl; // 仍是向左對齊
  cout.width(9);    // 設定寬度為 9 個字元
  cout << internal << "Good" << endl
       << right    << "Good" << endl;  // 串接輸出
}
