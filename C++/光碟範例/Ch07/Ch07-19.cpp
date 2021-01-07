#include <iostream>
#include <cstring>
#include <cctype>       // 使用 toupper() 需含括此檔
using namespace std;

char *toUpper(const char *);   // 宣告函式傳回值為字元指標

int main(void)
{
  cout << toUpper("happy Birthday");
}

char *toUpper(const char* ptr)        // 將字串所有小寫字母
{                                     // 轉成大寫的函式
  unsigned len = strlen(ptr);
  char *newStr = new char[len];       // 建立一新字串
  for(unsigned i=0;i<len;i++)
    *(newStr+i) = toupper(*(ptr+i));  // 將字元轉成大寫

  return newStr;        // 傳回轉換後的字串
}
