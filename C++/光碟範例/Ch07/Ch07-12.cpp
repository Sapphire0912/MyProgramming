#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char str[]="How are you?";
  char *ptr = str;

  for (unsigned i=0;i<strlen(str);i++)
    cout << *(str+i); // 將陣列名稱 str 當成指標
  cout << endl;

  for (unsigned i=0;i<strlen(ptr);i++)
    cout << ptr[i];   // 將指標 ptr 當成陣列名稱使用
}
