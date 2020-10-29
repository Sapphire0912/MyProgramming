#include <iostream>
using namespace std;

inline double FtoC (double f)   // ﹚竡︽ずㄧΑ
{
  return (f - 32) * 5 / 9;
}

int main()
{
  double F;
  cout << "叫块地ん放";
  cin >> F;

  cout << "传衡Θ尼ん放 " << FtoC(F) << " ";
}
