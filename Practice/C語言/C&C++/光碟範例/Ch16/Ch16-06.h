// ㄧΑ妓
// т皚い程┮竚
template<class T,int size> // 穝糤獶妓把计
int min(T (&data)[size])
{
  int index = 0; // 魁程竚

  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}