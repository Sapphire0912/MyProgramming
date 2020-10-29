#include <iostream>
using namespace std;
void adding(void);     //⊿Τ肚の把计

int main()
{
  for (int i=0;i<3;i++)     // ㊣ adding() Ω
    adding();
}

void adding(void)
{
  static int number=100;  // 繰篈Ы场跑计
  cout << "number = " << number++ << endl;
}
