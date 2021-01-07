#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  fstream file;     // 先建構物件

  file.open("c:\\test.txt", ios_base::out); // 開啟可寫入的檔案
  if (!file)                    // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    file << "測試一下" << endl; // 寫入一行文字
    file.close();               // 關閉檔案
    cout << "寫入完畢" << endl;
  }                                                          

  file.open("c:\\test.txt", ios_base::app); // 以附加的方式開啟
  if (!file)                    // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    for (int i = 0; i<10; i++)  // 用迴圈在檔案後面
      file << i;                // 加上數字 0 到 9
    cout << "寫入完畢" << endl;
  }
}
