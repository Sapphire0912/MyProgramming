#include <iostream>
using namespace std;

int main()
{
  int   *iptr,age=18;         // 宣告整數型別指標與變數
  float *fptr,weight=65.05f;  // 宣告浮點數型別指標與變數
  char  *cptr,bloodtype='O';  // 宣告字元型別指標與變數
  iptr=&age;                  // iptr 指向 age 的位址
  fptr=&weight;               // fptr 指向 weight 的位址
  cptr=&bloodtype;            // cptr 指向 bloodtype 的位址

  cout << "年齡：" << *iptr <<  "歲" << endl;
  cout << "體重：" << *fptr <<  "公斤" << endl;
  cout << "血型：" << *cptr <<  "型" << endl;
}
