#include <iostream>
using namespace std;

int main()
{
  int a[5] = { 1,22,333,4444,55555};
  int *ptr = a;

  for(int i=0;i<5;i++)
    cout << "指標 ptr+" << i << " 的位址：" << (ptr+i)
         << "\t所指的記憶體存放的資料為：" << *(ptr+i) << endl;
}
