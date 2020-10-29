#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char str1[60];   // 先宣告兩個用以存放
  char str2[60];   // 使用者輸入字串的陣列

  cout << "請輸入第 1 個字串：";
  cin.getline(str1,80);      // 讓 cin 可取得一整行的輸入內容
  cout << "請輸入第 2 個字串：";
  cin.getline(str2,80);      // 讓 cin 可取得一整行的輸入內容

  if(strcmp(str1,str2) == 0) // 比對 str1、str2 的內容是否相同
    cout << "兩次輸入的字串的內容相同";
  else
    cout << "兩次輸入的字串內容不同";
}
