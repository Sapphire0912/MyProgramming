#include <iostream>
#include <cstring>   // 因為用到 strlen(), 故含括此檔案
using namespace std;

int main()
{
  char name[80];

  cout << "請輸入一字串：";
  cin.getline(name,80);      // 讓 cin 可取得一整行的輸入內容

  cout << "sizeof(name) = " << sizeof(name) << endl;
  cout << "strlen(name) = " << strlen(name) << endl;
}
