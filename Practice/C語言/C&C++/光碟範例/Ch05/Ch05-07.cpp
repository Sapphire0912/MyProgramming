#include<iostream>
using namespace std;

int main()
{
  double fee = 100;      // 票價 100 元
  int ticket;
  cout << "要買幾張票？";
  cin >> ticket;

  fee *= (ticket <10) ? (ticket) : (ticket*0.8);
  cout << "您要購買 " << ticket << " 張票" << endl
       << "共計 " << fee << " 元";
}
