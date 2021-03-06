// 函式樣版
// 找出陣列中的最小值所在的位置
template<class T,int size> // 新增非型別的樣版參數
int min(T (&data)[size])
{
  int index = 0; // 紀錄最小值的位置

  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}