#include<iostream>
#include<string>
using namespace std;

int main()
{
  char ss[30];
  cout << "請輸入一個字串：";
  cin.getline(ss, 10, '$');
  cout << ss << endl;

  cout << "請輸入一個字串：";
  cin.get(ss, 30);
  cout << ss << endl;
  cout << "請輸入一個字串：";
  cin.get(ss, 30);
  cout << ss << endl;
}
