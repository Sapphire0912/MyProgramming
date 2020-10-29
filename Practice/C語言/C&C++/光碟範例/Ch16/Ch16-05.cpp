#include <iostream>
#include "Ch16-04.h"
using namespace std;

int main()
{
  int all[] = {20,17,39,18,22,46}; // 測試資料
  double another[] = {7.65,3.4,2.11,1.5,4.33}; // 測試資料

  int minOfAll = min(all,sizeof(all) / sizeof(int));
  cout << "all[] 中最小的元素是 all[" << minOfAll 
       << "]" << endl;
  
  minOfAll = min(another,sizeof(another) / sizeof(double));
  cout << "another[] 中最小的元素是 another[" << minOfAll 
       << "]" << endl;
}
