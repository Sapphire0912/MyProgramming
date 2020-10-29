#include<iostream>
#include<string>
#include<exception>        // 使用 exception 類別需含括此檔
using namespace std;

int main()
{
  int* ptr;
  string s = "Exception";  // 測試用的字串物件
  long num;

  try {
    cout << "請輸入要配置的 int 陣列元素數量：";
    cin >> num;
    ptr = new int[num];

    cout << "請問要檢視字串中的第幾個字元：";
    cin >> num;
    cout << s.at(num);
  }
  catch (exception e) { // 補捉 exception 類別及其衍生類別的例外
    cerr << "\n...很抱歉，發生無法處理的問題：" << e.what()
         << "，程式必須結束...";
  }

  delete [] ptr;
  cout << "\n程式結束！\n";
}
