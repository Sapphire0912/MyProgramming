#include <iostream>
using namespace std;
void swap(int&,int&);

int main()
{
  int a=5,b=10;
  cout << " main()い..." << endl;
  cout << "ユ传玡 a = " << a << "  b = " << b << endl;
  cout << "跑计 a  " << &a << endl;
  cout << "跑计 b  " << &b << endl;

  swap(a,b); // ㊣ㄧΑ, 盢跑计 a,b 讽Θ把计
  cout << "\n main()い..." << endl;
  cout << "ユ传 a = " << a << "  b = " << b << endl;
}

void swap(int &i,int &j)    // 盢ㄢ把计癸秸ㄧΑ
{
  int temp;         // 既跑计
  temp = i;
  i = j;
  j = temp;
  cout << "\n swap() ㄧΑい..." << endl;
  cout << "ユ传い i = " << i << "  j = " << j << endl;
  cout << "跑计 i  " << &i << endl;
  cout << "跑计 j  " << &j << endl;
}
