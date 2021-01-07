#include <iostream>
using namespace std;

void FtoC (double f)      // 盢地ん放锣Θ尼んㄧΑ
{
  cout << "传衡Θ尼ん放 "
       <<  ((f - 32) * 5 / 9) << " ";  // 放锣传そΑ衡Α
}

int main()
{
  double x;
  cout << "叫块地ん放";
  cin >> x;
  FtoC(x);               // ノ x 把计㊣ FtoC()
}
