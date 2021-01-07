#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char str1[]="Lazy Boy";
  char str2[]="Cute Girl";
  char str3[]="Pink Panther";
  cout << "第 1 個字串：" << str1 << '\n'
       << "第 2 個字串：" << str2 << '\n'
       << "第 3 個字串：" << str3 << endl;

  strcpy(str2,str1);    // 將字串1 複製到字串 2
  cout << "將第 1 個字串全部複製到第 2 個字串：" << '\n'
       << "第 2 個字串：" << str2 << endl;

  int n;
  cout << "要複製第 1 個字串的前幾個字元到第 3 個字串：";
  cin >> n;
  strncpy(str3,str1,n); // 將字串 1 的前 n 個字元複製到字串 3
  cout << "將第 1 個字串前 " << n << " 個字複製到第 3 個字串："
       << "\n第 3 個字串：" << str3;
}
