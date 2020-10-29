#include <iostream>
#include <fstream>       // 使用檔案串流
using namespace std;

int main()
{
  ifstream file1("Ch14-01.cpp");
  fstream file2;             // 先建構物件
  file2.open("Ch14-02.cpp"); // 再開啟檔案

  if (!file1 || !file2)       // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    char str[80];
    file1.getline(str,80); // 從 file1 讀一行內容
    cout << str << endl;   // 輸出讀到的內容

    file2.getline(str,80); // 從 file2 讀一行內容
    file2.getline(str,80); // 再從 file2 讀一行內容
    cout << str;           // 輸出第 2 次讀到的內容
  }
} // 解構函式會自動關閉檔案
