#include<iostream>
#include<cstring>
using namespace std;

class Str {          // 陽春的字串類別
public:
  void show() { cout << data; }
  Str(const Str&);
  Str(const char * ptr);
  Str(int);
private:
  char * data;     // 指向字串的指標
  int len;         // 字串長度
};

Str::Str(const char *s)
{
  len = strlen(s);
  data = new char[len+1];   // 配置新的記憶體空間
  strcpy(data, s);          // 將字串內容複製到新的空間
}

Str::Str(int n=10)           // 只有指定字串長度的建構函式
{
  if ( n <= 0);              // 若參數值不大於 0
    n = 10;                  // 就一律將長度設為 10
  len = n;
  data = new char[len+1];
  for(int i=0; i<n; i++)     // 將新配置的空間填上空白
    data[i] = ' ';
  data[n] = 0;               // 在字串最後面加上結束字元
}

Str::Str(const Str& s)
{
  len = s.len;               // 複製字串長度
  data = new char[len+1];    // 先配置新空間
  strcpy(data, s.data);      // 再複製字串
}
