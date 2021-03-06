#include <iostream>
using namespace std;

// 函式宣告
int min(int data[],int size);

int main()
{
  int all[] = {20,17,39,18,22,46}; // 測試資料
  int minOfAll = min(all,sizeof(all) / sizeof(int));

  cout << "all[] 中最小的元素是 all[" << minOfAll 
       << "]" << endl;
}

// 找出陣列中的最小值所在的位置
int min(int data[],int size)
{
  int index = 0; // 紀錄最小值的位置
  
  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}