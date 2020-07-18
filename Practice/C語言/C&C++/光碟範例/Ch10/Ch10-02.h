#include<iostream>
#include<cstring>
#include<cctype>    // 用到字元轉換函式
using namespace std;

class Str {          // 陽春的字串類別
public:
  void show() { cout << data; }
  Str(const Str&);
  Str(const char * ptr);
  Str(int);
  ~Str() { delete [] data; }  // 解構函式
  bool operator!() { return len==0; }  // 若字串長度為 0 即傳回真
  Str operator+();    // 將字串變成大寫
  Str operator-();    // 若字串變成小寫
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

Str::Str(int n=0)           // 只有指定字串長度的建構函式
{
  if ( n < 0)               // 若參數為負值
    n = 0;                  // 就將長度設為 0
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

Str Str::operator+()
{
  char* temp = new char[len];
  strcpy(temp,data);
  for(int i=0; i<len; i++)   // 將字元變成大寫的迴圈
    temp[i]=toupper(temp[i]);// 呼叫函式將字元變成大寫
  return Str(temp);
}

Str Str::operator-()
{
  char* temp = new char[len];
  strcpy(temp,data);
  for(int i=0; i<len; i++)   // 將字元變成小寫的迴圈
    temp[i]=tolower(temp[i]);// 呼叫函式將字元變小寫
  return Str(temp);
}
