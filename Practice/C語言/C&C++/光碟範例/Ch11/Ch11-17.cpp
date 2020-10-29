#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int main()
{
  string s;
  cout << "請輸入一個字串：";
  cin >> s;

  int len = s.size();
  char* cstr = new char(len+1);
  strcpy(cstr,s.c_str());  // 複製字串

  for (int i=0; i<len-2; i++) // 排序字元陣列內容
    for (int j=i+1; j<len-1; j++)
      if (cstr[i]>cstr[j]) {
        char tmp = cstr[i];
        cstr[i] = cstr[j];
        cstr[j] = tmp;
      }

  cout << "將字串內容排序後：" << cstr;
  delete [] cstr;
}
