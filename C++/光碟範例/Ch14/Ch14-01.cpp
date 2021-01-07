#include<iostream>
using namespace std;

int main()
{
  wcout.imbue(locale("cht"));   // 設定使用中文
  wcout << L"請輸入一個數字：";

  int i;
  wcin >> i;
  wcerr.imbue(locale("cht"));   // 設定使用中文
  wcerr << L"測試 wcerr：" << ++i << endl;
  wclog.imbue(locale("cht"));   // 設定使用中文
  wclog << L"測試 wclog：" << ++i << endl;
}
