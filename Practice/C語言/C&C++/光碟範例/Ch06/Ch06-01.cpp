#include <iostream>
using namespace std;

void beep()       // 定義一個 beep() 函式
{
  cout << "工作完成\a\n";   // 讓電腦發出嗶聲
}

int main()
{
  cout << "現在開始處理工作" << endl;

  for (int i=0; i < 50000000; i++)
    ; // 用執行五千萬次加法及比較的迴圈模擬電腦在做一件事
  beep();        // 處理完畢, 呼叫 beep() 函式

  for (int i=0; i < 80000000; i++)
    ; // 用執行八千萬次加法及比較的迴圈模擬電腦在做另一件事
  beep();        // 處理完畢, 呼叫 beep() 函式
}
