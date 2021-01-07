#include<iostream>
#include<iomanip>
#include<string>
using namespace std;

int main()
{
  cout << "請輸入一個字串：";
  string ss;
  cin >> setw(5) >> ss;
  cout << "ss = " << ss << endl;

  cout << "請輸入另一個字串：";
  cin >>  ss;
  cout << "ss = " << ss;
}
