#include<iostream>
using namespace std;

int main()
{
  int num1,num2;
  cout << "計算兩整數的最大公因數\n";
  cout << "請輸入第1個數字：";
  cin >> num1;
  cout << "請輸入第2個數字：";
  cin >> num2;

  int a, b = num1, c=num2;  // c 的值就是第 1 次相除的餘數
  do {
    a=b;
    b=c;
    c=a%b;             // 輾轉相除, 取餘數
  } while (c!=0);      // 當餘數為 0 時, b 就是最大公因數

  cout << num1 << " 和 " << num2 << " 的最大公因數是："
       << b;
}
