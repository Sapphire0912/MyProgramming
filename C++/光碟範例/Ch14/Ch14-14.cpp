#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
  string filename;
  cout << "請輸入要寫入的檔案名稱：";
  cin >> filename;

  ifstream file(filename.c_str(),ios_base::binary);   // 開啟二元檔
  if (!file)                        // 若無法開啟檔案
    cerr << "檔案開啟失敗" << endl;
  else {
    cout << "目前讀取位置在：" << file.tellg() << endl;

    double d;
    file.seekg(5 * sizeof(double));      // 跳到第 6 筆
    cout << "目前讀取位置在：" << file.tellg() << endl;
    file.read((char*) &d, sizeof(double));
    cout << d << endl;
    cout << "目前讀取位置在：" << file.tellg() << endl;

                                    // 跳到倒數第 2 筆
    file.seekg(-2*sizeof(double),ios_base::end);
    cout << "目前讀取位置在：" << file.tellg() << endl;
    file.read((char*) &d, sizeof(double));
    cout << d << endl;
    cout << "目前讀取位置在：" << file.tellg() << endl;
  }
}
