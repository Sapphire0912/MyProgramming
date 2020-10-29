#include<iostream>
using namespace std;

int main()
{
  int i = 5;
  float j = 3.5;

  i *= 4;    // 相當於 i = i * 4
  j /= 2;    // 相當於 j = j / 2
  cout << "i  = " << i << endl
       << "j  = " << j << endl;
}
