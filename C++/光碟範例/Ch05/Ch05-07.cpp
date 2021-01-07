#include<iostream>
using namespace std;

int main()
{
  double fee = 100;      // 布基 100 じ
  int ticket;
  cout << "璶禦碭眎布";
  cin >> ticket;

  fee *= (ticket <10) ? (ticket) : (ticket*0.8);
  cout << "眤璶潦禦 " << ticket << " 眎布" << endl
       << "璸 " << fee << " じ";
}
