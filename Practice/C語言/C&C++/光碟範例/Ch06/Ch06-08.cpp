#include <iostream>
using namespace std;
int x=10;   // 办跑计

int main()
{
  int x=100;
  cout << "Ы场跑计 x = " << x << '\t'
       << "办跑计 x = " << ::x << endl;  // ノ :: 办跑计

  x += ::x++;

  cout << "Ы场跑计 x = " << x << '\t'
       << "办跑计 x = " << ::x << endl;
}
