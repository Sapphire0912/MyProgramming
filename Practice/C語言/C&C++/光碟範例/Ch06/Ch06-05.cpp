#include <iostream>
using namespace std;
void adding();          //沒有傳回值及參數, 需註明為 void

int main()
{
  for (int i=0;i<3;i++) // 呼叫 adding() 三次
    adding();
}

void adding(void)
{
  int number=100;       // 局部變數, 有初始值
  cout << "number = " << number++ << endl;
}
