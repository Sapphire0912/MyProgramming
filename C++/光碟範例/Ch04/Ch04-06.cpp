#include<iostream>

int main()
{
  int i = 10, j;
  j = (i++) + i + (i++);  // 兩個後置遞增
  std::cout << "i = " << i << "\t\tj = " << j << '\n';

  i = 10;                // 將 i 再設為 10
  j = (--i) + i + (--i);  // 兩個前置遞減
  std::cout << "i = " << i << "\t\tj = " << j;
}
