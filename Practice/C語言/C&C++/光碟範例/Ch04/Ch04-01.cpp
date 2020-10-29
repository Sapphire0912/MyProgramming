#include<iostream>

int main()
{
  int i,j;
  i = (1 + 3) * 5 + 6;   // -> 4 * 5 + 6
  j = 1 + 3 * (5 + 6);   // -> 1 + 3 * 11
  std::cout << "跑计 i 单" << i
            << "\n跑计 j 单" << j;
}
