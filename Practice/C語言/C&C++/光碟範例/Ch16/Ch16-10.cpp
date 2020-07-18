#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int all[] = {20,17,39,18,22,46}; // 測試資料
  double another[] = {7.65,3.4,2.11,1.5,4.33}; // 測試資料
  
  // 使用min_element()函式樣版處理整數陣列
  int* minInt = min_element<int*>(&all[0],&all[6]);
  cout << "all[] 中最小的元素是 " << *minInt << endl;

  // 使用min_element()函式樣版處理雙精度陣列
  double* minDouble = 
    min_element<double*>(&another[0],&another[5]);
  cout << "another[] 中最小的元素是 " << *minDouble << endl;
}
