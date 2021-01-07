#include <iostream>
using namespace std;
void showresult(double); // 沒有傳回值的函式
                             // 要宣告為 void
int main()
{
  int sex;                   // 代表性別選項
  double height, weight;     // 身高與體重

  do {  // 利用迴圈要求使用者一定要選擇 1 或 2
    cout << "性別:(1)男(2)女：";
    cin >> sex;
  } while (sex!=1 && sex!=2);

  cout << "請輸入身高(公分)：";
  cin >> height;

  if (sex == 1)
    weight = (height - 80)*0.7; // 男性的標準體重公式
  else
    weight = (height - 70)*0.6; // 女性的標準體重公式

  showresult(weight);           // 呼叫顯示結果的函式
}

void showresult(double result)  // 定義輸出結果的函式
{
  cout << "您的標準體重範圍是 " << endl << result * 0.9
       << " 公斤至 " << result * 1.1 << " 公斤之間";
}
