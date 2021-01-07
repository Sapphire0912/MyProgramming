#include <iostream>
using namespace std;

// ㄧΑ
int min(int data[],int size);

int main()
{
  int all[] = {20,17,39,18,22,46}; // 代刚戈
  int minOfAll = min(all,sizeof(all) / sizeof(int));

  cout << "all[] い程じ琌 all[" << minOfAll 
       << "]" << endl;
}

// т皚い程┮竚
int min(int data[],int size)
{
  int index = 0; // 魁程竚
  
  for(int i = 1;i < size;i++) {
    if(data[i] < data[index])
      index = i;
  }
      
  return index;
}