#include <iostream>
using namespace std;

class ByteInt {
public:
  ByteInt(int i) { c = (char) i; }  // 建構函式
  void show()    { cout << (int) c << endl; }
  ByteInt &operator++();         // 前置遞增函式
  ByteInt operator++(int);       // 後置遞增函式
private:
  char c;       // 用來存放數值的資料成員
};

ByteInt& ByteInt::operator++()   // 前置遞增函式
{
  c++;
  cout << "前置 ++" << endl;     // 此行可刪除
  return *this;
}

ByteInt ByteInt::operator++(int) // 後置遞增函式
{
  ByteInt tmp = *this;           // 保存遞增前的值
  c++;
  cout << "後置 ++" << endl;     // 此行可刪除
  return tmp;                    // 傳回遞增前的值
}

void main()
{
  ByteInt b(5);
  (++b).show(); // 加 1 後顯示其值
  (b++).show(); // 再加 1, 但顯示加 1 之前的值
  b.show();     // 顯示最後結果
}
