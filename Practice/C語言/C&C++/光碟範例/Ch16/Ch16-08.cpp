#include <iostream>
#include "Ch16-08.h"
using namespace std;

int main()
{
  char* all[] = { // 測試資料
    "zebra",
    "dog",
    "cat",
    "frog",
  };
  
  // 套用到字串陣列上
  int minOfAll = min<char*>(all,4); 
    
  cout << "all[] 中最小的元素是 all[" << minOfAll 
       << "]" << endl;
}