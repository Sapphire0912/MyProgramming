#include <iostream>
#include <cstring>
using namespace std;
#define LEN 80      // 定義字元陣列長度
void sort(char [][LEN], int);

int main()
{
  char str[][LEN] = {"Taipei", "Taoyuan", "Hsinchu",
                     "Miaoli", "Ilan", "Chiayi"};

  sort(str,6);      // 將 str 排序, 共有 6 個字串

  for (int i=0;i<6;i++)   // 輸出排序後的結果
    cout << str[i] <<endl;
}

void sort (char str[][LEN], int count)
{
  char temp[LEN];               // 對調字串時的暫存陣列
  for(int i=0;i<count-1;i++)    // 用迴圈來比較字串的大小
     for(int j=i+1;j<count;j++)
       if(strcmp(str[i],str[j])>0) { // 比較字串
         strcpy(temp,str[j]);        //
         strcpy(str[j],str[i]);      // 對調字串
         strcpy(str[i],temp);        //
       }
}
