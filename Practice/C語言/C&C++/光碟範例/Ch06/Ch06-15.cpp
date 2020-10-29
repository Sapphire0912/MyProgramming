#include <iostream>
#include <ctime>
using namespace std;

int main()
{
  cout << "執行加法及比較運算一億次需要 ";
  clock_t starttime = clock();
  for(int i=0;i<100000000;i++) ;   // 沒有做事的迴圈
  clock_t endtime = clock();

  cout << (double)(endtime - starttime) / CLK_TCK << " 秒" ;
}
