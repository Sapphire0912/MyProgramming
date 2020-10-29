#include<iostream>
#include<cstring>
#include<cctype>
#include<cassert>       // 使用 assert() 函式需含括的檔案
using namespace std;

class Str {             // 陽春的字串類別
public:
  void show() { cout << data; }
  Str(const Str&);
  Str(const char * ptr);
  Str(int);
  ~Str() { delete [] data; }  // 解構函式
  bool operator!() { return len==0; }  // 若字串長度為 0 即傳回真
  Str operator+();    // 將字串變成大寫
  Str operator-();    // 若字串變成小寫
  Str operator+(Str);    // 與另一物件相加
  Str operator+(char *); // 與指標所指的字元相加
  char& Str::operator[](int i)
  {
     assert(i>-1 && i < len);  // 檢查是否超過範圍
     return data[i];           // 傳回字元的參考
  }
  Str& Str::operator=(const Str&);   // 將同型物件指定給自己
  Str& Str::operator=(const char*);  // 將字串常數指定給自己
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
  if ( n < 0)               // 若參數值為負
    n = 0;                  // 就長度設為 0
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

Str Str::operator+()         // 將全部字元變大寫
{
  char* temp = new char[len];
  strcpy(temp,data);
  for(int i=0; i<len; i++)   // 將字元變成大寫的迴圈
    temp[i]=toupper(temp[i]);// 呼叫函式將字元變成大寫
  return Str(temp);
}

Str Str::operator-()         // 將全部字元變小寫
{
  char* temp = new char[len];
  strcpy(temp,data);
  for(int i=0; i<len; i++)   // 將字元變成大寫的迴圈
    temp[i]=tolower(temp[i]);// 呼叫函式將字元變成大寫
  return Str(temp);
}

Str Str::operator+(Str s)
{
  Str tmp(len + s.len);      // 先建立暫存物件
                             // 設定長度為兩字串的長度和
  strcpy(tmp.data, data);    // 複製前半字串
  strcat(tmp.data, s.data);  // 複製後半字串
  return tmp;  // 將串接的結果傳回, 以參與後續的運算
}

Str Str::operator+(char* ptr)
{
  Str tmp(len + strlen(ptr));// 先建立暫存物件
                             // 設定長度為兩字串的長度和
  strcpy(tmp.data, data);    // 複製前半字串
  strcat(tmp.data, ptr);     // 複製後半字串
  return tmp;  // 將串接的結果傳回, 以參與後續的運算
}

Str& Str::operator=(const Str& s)
{
  if(this != &s)                                     
    return *this = s.data;  // 傳回呼叫另一版本的結果
  return *this;             // 傳回物件本身          
}

Str& Str::operator=(const char* s)
{
  delete [] data;       // 釋放原指標所指記憶體
  len = strlen(s);
  data = new char[len+1];
  strcpy(data, s);      // 複製字串
  return *this;         // 傳回物件的參考
}
