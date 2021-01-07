#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
  string filename;
  cout << "請輸入要讀取的檔案名稱：";
  cin >> filename;

  ifstream file(filename.c_str());  // 開啟唯讀檔案
  if (!file)                        // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    char ch;
    while(!file.get(ch).eof())      // 若還沒到檔案結尾
      cout << ch;                   // 關閉檔案
  }
}
