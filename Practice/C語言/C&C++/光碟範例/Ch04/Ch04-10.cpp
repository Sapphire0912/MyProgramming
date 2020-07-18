#include<iostream>
using namespace std;

int main()
{
  short i = 23, j = 14;

  cout << "i >> 1 = " << (i >> 1) << endl;
  cout << "i << 3 = " << (i << 3) << endl;
  cout << "~i = " << (~i) << '\n' << endl;

  cout << "i = " << i << "\tj =" << j << endl;

  cout << "i & j = " << (i & j) << endl;
  cout << "i | j = " << (i | j) << endl;
  cout << "i ^ j = " << (i ^ j) << endl;
}
