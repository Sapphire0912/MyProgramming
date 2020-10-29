#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
  cout << "請輸入一個數字：";
  int i;
  cin >> hex >> i;
  cout << showbase;
  cout << i << " 換算成8進位為 "  << oct << i << endl;
  cout << i << " 換算成16進位為 " << hex << i << endl;;

  cout << "請再輸入一個數字：";
  cin >> i;
  cout << uppercase;
  cout << i << " 換算成10進位為 " << setbase(10)<< i << endl;
  cout << i << " 換算成8進位為 "  << setbase(8) << i;
}
