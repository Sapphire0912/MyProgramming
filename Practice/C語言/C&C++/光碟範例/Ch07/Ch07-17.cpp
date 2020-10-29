#include <iostream>
using namespace std;
void swap(int*,int*);

int main()
{
  int a=5,b=10;
  cout << " main()い..." << endl;
  cout << "ユ传玡 a = " << a << "  b = " << b << endl;
  cout << "跑计 a  " << &a << endl;
  cout << "跑计 b  " << &b << endl;

  swap(&a,&b); // ㊣ㄧΑ, 盢跑计 a,b 讽Θ把计
  cout << " main()い..." << endl;
  cout << "ユ传 a = " << a << "  b = " << b << endl;
}

void swap(int *a,int *b)    // 盢ㄢ把计癸秸ㄧΑ
{
  int temp;         // 既跑计
  temp = *a;
  *a = *b;
  *b = temp;
  cout << " swap() ㄧΑい..." << endl;
  cout << "ユ传い a = " << *a << "  b = " << *b << endl;
  cout << "跑计 a  " << a << endl;
  cout << "跑计 b  " << b << endl;
}
