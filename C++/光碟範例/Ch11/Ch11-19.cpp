#include<iostream>
#include<string>
#include<cctype>
using namespace std;

bool checkID (string idStr)          // 查驗身份證字號的函式
{
  int letterNums[] = {10,11,12,13,14,15,16,17,34,18,
                      19,20,21,22,35,23,24,25,26,27,
                      28,29,32,30,31,33};

  if (islower(idStr[0]))        // 先將第一個英文字母轉為大寫
    idStr[0] = toupper(idStr[0]);

  int total = (letterNums[idStr[0] - 'A'] / 10) +
              (letterNums[idStr[0] - 'A'] % 10) * 9;
  for(int i = 1;i < 9;i++)
    total += (idStr[i] - '0') * (9 - i); // 依序加總

  // 以10減去加總值之個位數後再取個位數
  int checkNum = (10 - total % 10) % 10;

  if(checkNum == (idStr[9] - '0'))  //與身份證字號最後一碼比
    return true;
  else
    return false;
}

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
           == string::npos)    // 檢查後 9 字是否含數字以外的字元
        if (isID = checkID(idStr))   // 呼叫 checkID() 進行查驗
          cout << "查驗通過" << endl;
        else
          cout << "不是合法的身份證字號" << endl;
      else
        cout << "身份證字號後面9個字應是數字！" << endl;
    else
      cout << "身份證字號第 1 個字應為英文字母！" << endl;
  } while (!isID);
}
