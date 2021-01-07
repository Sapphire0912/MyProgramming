#include <iostream>
using namespace std;

double stdWeight(int sex, double height)  // 體重計算函式
{
  if (sex == 1)     // 男
    return (height - 80) * 0.7;
  else              // 女
    return (height - 70) * 0.6;
}

int main()
{
  int sex;               // 代表性別選項
  double height, weight; // 身高及體重

  do {  // 一定要選擇 1 或 2
    cout << "性別(1)男(2)女：";
    cin >> sex;
  } while (sex!=1 && sex!=2);

  cout << "請輸入身高(公分)：";
  cin >> height;

  weight = stdWeight(sex, height);
  cout << "您的標準體重範圍是 " << endl << weight * 0.9
       << " 公斤至 " << weight * 1.1 << " 公斤之間";
}
