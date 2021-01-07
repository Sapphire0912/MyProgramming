#include <cstring>

// 樣版函式
// 找出陣列中的最小值所在的位置
template<class T>
int min(T data[],int size)
{
  int index = 0; // 紀錄最小值的位置
  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}

// 為 char* 特製的 min() 函式樣版
template<>
int min<char*>(char* data[],int size) 
{
  int index = 0;
  for(int i = 1;i < size;i++) {
    // 改採用 strcmp 函式比較字串內容
    if(strcmp(data[i],data[index]) < 0)
      index = i;
  }
  return index;
}
