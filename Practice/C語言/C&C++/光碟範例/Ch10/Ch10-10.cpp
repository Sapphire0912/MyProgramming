#include <iostream>
using namespace std;

class ByteInt {
public:
  ByteInt(int i) { c = (char) i; }  // 建構函式
  void show()    { cout << (int) c << endl; }
  operator int() { return (int) c; }  // 將物件轉型為整數
  ByteInt &operator++();        // 前置遞增函式
  ByteInt operator++(int);      // 後置遞增函式
private:
  char c;       // 用來存放數值的資料成員
};

ByteInt& ByteInt::operator++()   // 前置遞增函式
{
  c++;
  return *this;
}

ByteInt ByteInt::operator++(int) // 後置遞增函式
{
  ByteInt tmp = *this;           // 保存遞增前的值
  c++;
  return tmp;                    // 傳回遞增前的值
}

void main()
{
  ByteInt b(0);
  for(;b<5;b++)      // 比較及遞增物件
    b.show();
  cout << "半徑為 " << b << " 的圓, 周長為 " // 直接輸出物件
       << 2 * b * 3.14159;                   // 用物件參與乘法計算
}
