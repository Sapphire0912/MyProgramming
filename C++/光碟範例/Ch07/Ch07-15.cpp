#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  int how_many;
  cout << "請問要計算多少個數字的算術及幾和平均：";
  cin >> how_many;

  double *dptr  = new double[how_many]; // 配置指定數量的記憶體

  for(int i=0;i<how_many;i++) {
    cout << "請輸入第 " << (i+1) << " 個數值：";
    cin >> *(dptr+i);
  }

  double sum = 0;
  for(int i=0;i<how_many;i++)        // 計算所有數值的總和
    sum += *(dptr+i);
  cout << "算數平均為：" << (sum / how_many) << endl;

  sum = 1;
  for(int i=0;i<how_many;i++)        // 計算所有數值的乘積
    sum *= *(dptr+i);
  cout << "幾何平均為：" << pow(sum,1.0/how_many);

  delete [] dptr;
}
