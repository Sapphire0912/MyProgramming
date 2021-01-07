#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
  string filename;
  cout << "請輸入要寫入的檔案名稱：";
  cin >> filename;
                                               // 開啟二元檔
  fstream file(filename.c_str(), ios_base::out|ios_base::binary);
  if (!file)                        // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    for (int i = 1; i<=10; i++) {
      double d = i * i * i;     // 計算 1～10 的立方
      file.write((char*) &d, sizeof(double));
    }
    file.close();
    cout << "寫入完畢" <<endl;
  }
                                               // 重新開啟檔案
  file.open(filename.c_str(), ios_base::in|ios_base::binary);
  if (!file)                        // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    for (int i = 1; i<=10; i++) {   // 用迴圈讀十個數字
      double d;
      file.read((char*) &d, sizeof(double));
      cout << d << endl;
    }
    file.close();
    cout << "讀取完畢";
  }
}
