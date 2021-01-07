#include<iostream>
using namespace std;

int main()
{
  char go_again = 'Y';
  float height, weight;

  while (go_again == 'Y' || go_again == 'y') { // 大小寫 Y 都會
    cout << "請輸入身高 (公分)：";             // 繼續迴圈
    cin >> height;
    cout << "請輸入體重 (公斤)：";
    cin >> weight;
    cout << "您的體脂率為：" << weight / (height * height) * 10000
         << '%' << endl;       // 體脂率為體重除以身高 (公尺) 平方
    cout << "要繼續計算另一位嗎？(要請輸入 Y 或 y )：";
    cin >> go_again;
  }
}
