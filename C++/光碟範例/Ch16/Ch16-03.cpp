#include <iostream>
using namespace std;

// ㄧΑ妓
// т皚い程┮竚
template<class T>
int min(T data[],int size)
{
  int index = 0; // 魁程竚

  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}

int main()
{
  int all[] = {20,17,39,18,22,46}; // 代刚戈
  double another[] = {7.65,3.4,2.11,1.5,4.33}; // 代刚戈

  int minOfAll = min<int>(all,sizeof(all) / sizeof(int));
  cout << "all[] い程じ琌 all[" << minOfAll 
       << "]" << endl;
  
  minOfAll = min<double>(another,
    sizeof(another) / sizeof(double));
  cout << "another[] い程じ琌 another[" << minOfAll 
       << "]" << endl;
}
