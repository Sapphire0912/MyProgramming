#include<iostream>
#include<string>
#include<cctype>
using namespace std;

int main()
{
  string idStr;      // 記錄使用者輸入資料
  bool isID = false; // 使用者輸入的格式是否正確
  string num = "0123456789";  // 用來檢證是否為數字的字串

  do {
    cout << "請輸入身份證字號：";
    cin >> idStr;
    if(idStr.size()!=10) {
      cout << "身份證字號共十個字元，請不要輸入空白！" << endl;
      continue;
    }
    if (isalpha(idStr[0]))  // 第 1 字是否為大寫或小寫英文字母
       if (idStr.substr(1,9).find_first_not_of("0123456789")
             == string::npos)  // 檢查後 9 字是否含數字以外的字元
         isID = true;
       else
         cout << "身份證字號後面9個字應是數字！" << endl;
    else
      cout << "身份證字號第 1 個字應為英文字母！" << endl;
  } while (!isID);
}
