#include <iostream>
using namespace std;
void adding(void);     //沒有傳回值及參數

int main()
{
  for (int i=0;i<3;i++)     // 呼叫 adding() 三次
    adding();
}

void adding(void)
{
  static int number=100;  // 靜態局部變數
  cout << "number = " << number++ << endl;
}
