#include <iostream>
#define SIZE 5               // 皚盽计
using namespace std;

int main()
{
  int numbers[SIZE];         // 纗计皚

  cout << "叫块 5 计, 祘Α盢т程" << endl;

  for (int i=0;i<SIZE;i++) { // ノ癹伴眔–じ
    cout << "叫块材 " << (i+1) << " 计";
    cin >> numbers[i];
  }

  int MAX = numbers[0];      // ノㄓ纗程跑计
                             // 砞材 1 じ

  for (int i=1;i<SIZE;i++)   // ゑ癸皚い┮Τじ癹伴
    if (numbers[i]>MAX)      // 璝 numbers[i]  MAX
      MAX = numbers[i];      // 玥盢程砞 numbers[i]

  cout << "块计い, 计程琌 " << MAX;
}
