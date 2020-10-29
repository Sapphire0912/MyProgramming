#include<iostream>
#include<stdexcept>            // 內含標準例外類別的宣告
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
  catch (bad_alloc e) {        // 捕捉配置記憶體失敗的例外
    cerr << e.what();          // 顯示例外的相關訊息
    cerr << "...您要求配置的陣列太大了...\n";
  }
  catch (out_of_range e) {     // 捕捉超出索引範圍的例外
    cerr << e.what();          // 顯示例外的相關訊息
    cerr << "...您要檢視的字元超出範圍...\n";
  }

  delete [] ptr;
  cout << "\n程式結束！\n";
}
