#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>    // 使用到 setw() 控制器
#include<cctype>     // 使用到 isupper()、islower() 函式
using namespace std;

int main()
{
  string filename;
  cout << "請輸入要讀取的檔案名稱：";
  cin >> filename;

  int count[26] = {0};             // 用來統計各字母字數的陣列
  fstream file(filename.c_str(), ios_base::in);
  if (!file)                       // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    char ch;
    while (!file.get(ch).eof())    // 未到檔案結尾前持續讀取
      if (isupper(ch))             // 若為大寫字母
        count[ch-65]++;            // 將對應位置的元素值加 1
      else if (islower(ch))        // 若為小寫字母
        count[ch-97]++;            // 將對應位置的元素值加 1
  }
  file.close();

  for(int i=0;i<26;i++) {  // 在螢幕上顯示統計結果
    cout << "字母" << char(65+i) << '/' << char(97+i) << "有 "
         << setw(3) << count[i] << " 個";
    cout << ((i%2)? '\n' : '\t');  // 每輸出兩筆就換行
  }
}