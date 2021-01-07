#include<iostream>
using namespace std;

class Car {   // 定義類別
public:       // 以下的成員是對外公開的
  double gas; // 載油量
  double eff; // 每公升可行駛公里數
};

int main()
{
  Car superone;
  superone.eff = 30;
  superone.gas = 20;
  cout << "超級省油車1公升可跑 " << superone.eff
       << " 公里" << endl;
  cout << "現在油箱有 " << superone.gas << " 公升油" << endl;

  float kilo;
  while(superone.gas > 0) {   // 若還有油
    cout << "現在要開幾公里：";
    cin >> kilo;
    if (superone.gas >= (kilo/superone.eff)) { // 若油量夠
      superone.gas -= kilo/superone.eff;       // 減掉用掉的油量
      if (superone.gas == 0)                   // 若油用完了
        cout << "沒油了！";
      else
        cout << "油箱還有 " << superone.gas << " 公升油" << endl;
    } else {                                   // 若油量不夠
      cout << "油量不夠，目前的油只夠跑 "
           << (superone.gas * superone.eff) << " 公里";
      break;
    }
  }
}
