#include<iostream>

int main()
{
  int i,j;
  i = (1 + 3) * 5 + 6;   // -> 4 * 5 + 6
  j = 1 + 3 * (5 + 6);   // -> 1 + 3 * 11
  std::cout << "變數 i 等於：" << i
            << "\n變數 j 等於：" << j;
}
