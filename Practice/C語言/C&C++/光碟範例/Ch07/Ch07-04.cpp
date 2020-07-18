#include <iostream>
#define SIZE 5              // 陣列大小常數
using namespace std;

int main()
{
  char array[SIZE]={'s','c','i','o','n'};

  cout << "排序前：";
  for (int i=0;i<SIZE;i++)    // 輸出排序前的陣列內容
    cout << array[i];

  for (int i=0;i<SIZE;i++)
    for (int j=i+1;j<SIZE;j++)
      if (array[i]<array[j])  // 若 array[i] 的值小於 array[j]
      {                       // 就將 2 個元素的值對調
        char temp = array[i]; // temp 是對調時用到的暫存變數
        array[i] = array[j];
        array[j] = temp;
      }

  cout << endl << "排序後：";
  for (int i=0;i<SIZE;i++)    // 輸出排序後的陣列內容
    cout << array[i];
}
