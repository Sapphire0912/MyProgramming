#include <iostream>
#include "Ch16-06.h"
using namespace std;

int main()
{
  int all[] = {20,17,39,18,22,46}; // 測試資料
  
  // 使用非型別的樣版參數
  int minOfAll = min<int,6>(all);
    
  // 編譯器會檢查陣列大小錯誤
  // minOfAll = min<int,8>(all);
  
  cout << "all[] 中最小的元素是 all[" << minOfAll 
       << "]" << endl;
}
