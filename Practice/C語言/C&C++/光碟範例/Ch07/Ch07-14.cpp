#include <iostream>
using namespace std;

int main()
{
  char a[3][4] = { "abc", "def", "ghi" };
  char (*str)[4] = a;       // 將二維陣列轉型為陣列指標

  for(int i=0;i<3;i++)
    cout << "指標 str+" << i << " 的位址：" << (str+i)
         << "\ta[" << i << "]的位址：" << &a[i] << endl;
  cout << endl;

  for(int i=0;i<3;i++)      // 將三個字串接續輸出
    cout << str[i];
}
