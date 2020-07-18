#include<iostream>
#include<string>
using namespace std;

int main()
{
  char array[] ="Happy new year!";
  string str[] = { string(),            // 空的字串物件
                   string(array),       // 從字元陣列建立字串
                   string(array,5),
                   string(array,6,3),
                   string(10, 'x')};    // 從字元建立字串

  for(int i=0;i<5;i++) {
    cout << "str[" << i << ']' << "的內容為：" << str[i] << endl
         << "\tsizeof()：" << sizeof(str[i])     // 顯示物件大小
         << "\tsize()：" << str[i].size()        // 顯示字串大小
         << "\tlength()：" << str[i].length() << endl;//字串長度
  }
}
