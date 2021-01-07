#include<iostream>
using namespace std;

int main()
{
  char beep = '\a';
  cout << "今天天氣很好\n"
       << "接著你會聽到三聲\"嗶聲\"\n";
  cout << "嗶!\t" << beep << "嗶!\t" << beep << "嗶!" << beep;
}
