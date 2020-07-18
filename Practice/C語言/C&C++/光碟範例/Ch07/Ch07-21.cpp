#include <iostream>
using namespace std;
int findmax(int[],int);
int findmin(int[],int);

int main()
{
   // 儲存各月份營業額的陣列
  int income[]={156548, 152074, 176325, 120159, 94876, 163584,
                179541, 146587, 156472, 135587, 95443, 169994};

  int i = findmax(income,12);
  cout << "營業額最高的是 " << (i+1) << " 月："
       << income[i] << " 元" << endl;
  i = findmin(income,12);
  cout << "營業額最低的是 " << (i+1) << " 月："
       << income[i] << " 元" << endl;
}

int findmax(int in[], int size)
{
  int max = 0;
  for (int i=1;i<size;i++)     // 找最大值的迴圈
    if(in[max] < in[i])
      max = i;

  return max;
}

int findmin(int in[], int size)
{
  int min = 0;
  for (int i=1;i<size;i++)     // 找最小值的迴圈
    if(in[min] > in[i])
      min = i;

  return min;
}
