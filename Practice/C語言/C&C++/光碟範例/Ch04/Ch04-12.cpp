#include<iostream>
using namespace std;

int main()
{
  int i,j,k;
  i = (j = (k = 1 + 2) + 3) + 4;
  cout << "i  = " << i << endl
       << "j  = " << j << endl
       << "k  = " << k << endl;
}
