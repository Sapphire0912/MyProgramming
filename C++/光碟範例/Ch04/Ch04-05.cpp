#include<iostream>

int main()
{
  int i = 100, j;
  j = (i++) + 5;   // 後置遞增
  std::cout << "i = " << i << "\t\tj = " << j;

  i = 100;
  j = (++i) + 5;   // 前置遞增
  std::cout << "\ni = " << i << "\t\tj = " << j;
}
