#include <iostream>
using namespace std;
#include "Ch16-09.h"

int main()
{
  char* all[] = { // 測試資料
    "zebra",
    "dog",
    "cat",
    "frog",
  };
  
  // 使用非型別的樣版參數
  int minOfAll = min<char*>(all,4); 
    
  cout << "all[] 中最小的元素是 all[" << minOfAll << 
    "]" << endl;
}