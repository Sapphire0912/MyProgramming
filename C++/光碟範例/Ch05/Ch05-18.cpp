#include<iostream>
using namespace std;

int main()
{
  int i=1;

  while (i>0) { // 無窮迴圈
    cout << "無窮迴圈執行中...\n";
    if (i == 5) // 當 i 為 5 時,
      break;    // 就跳出迴圈
    i++;
  }
  cout << "成功的跳出迴圈了！";
}
