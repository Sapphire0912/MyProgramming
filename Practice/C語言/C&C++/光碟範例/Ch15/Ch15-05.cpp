#include<iostream>
#include<string>
using namespace std;

int main()
{
  int* ptr;
  string s = "Exception";      // 測試用的字串物件
  long num;

  try {
    cout << "請輸入要配置的 int 陣列元素數量：";
    cin >> num;
    ptr = new int[num];

    cout << "請問要檢視字串中的第幾個字元：";
    cin >> num;
    cout << s.at(num);
  }
  catch (...) {                // 可補捉所有例外的 catch 區塊
    cerr << "\n...很抱歉，發生程式無法處理的問題，程式必須結束執行...";

  }

  delete [] ptr;
  cout << "\n程式結束！\n";
}
