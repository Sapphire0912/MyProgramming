#include<iostream>
#include<fstream>
#include<string>
using namespace std;

class Entry {   // 通訊錄項目類別
friend istream& operator>>(istream&, Entry&);
friend ostream& operator<<(ostream&, Entry&);
public:
  void keyin();
  string getname() { return name;}
  string getphone() { return phone;}
private:
  string name;  // 姓名
  string phone; // 電話
};

void Entry::keyin()     // 請使用者輸入新資料的函式
{
  cin.get();    // 清除緩衝區中的換行字元
  cout << "請輸入新建項目的姓名：";
  getline(cin,name);
  cout << "請輸入新建項目的電話號碼：";
  getline(cin,phone);
}

ostream& operator<<(ostream& os, Entry &e)
{ // 存檔時, 每筆資料存一行, 姓名與電話用逗號分開
  return os << e.name << ',' << e.phone << endl;
}

istream& operator>>(istream& is, Entry &e)
{
  getline(is,e.name,',');       // 先讀逗號之前的姓名
  getline(is,e.phone,'\n');     // 再讀換行字元之前的電話
  return is;
}

void addone(fstream& file)      // 輸入新項目的函式
{
  Entry newone;
  newone.keyin();
  file.seekp(0,ios_base::end);  // 移到檔案最後寫入新資料
  file << newone;
  cout << "已存檔!\n";
}

void lookup(fstream& file)      // 搜尋的函式
{
  cout << "要找誰的電話：";
  string name;
  cin.get();            // 清除緩衝區中的換行字元
  getline(cin,name);    // 由鍵盤取得姓名字串

  Entry who;            // 用來儲存由檔案讀入的資料
  file.seekg(0,ios_base::beg);  // 從頭讀取
  while(!file.eof()) {
    file >> who;
    if(name == who.getname()) { // 比對姓名
      cout << "電話號碼是 " << who.getphone() << '\n';
      return;           // 已經找到, 可跳出函式
    }
  }
  file.clear();         // 清除 eof() 的狀態
  cout << "沒有這個人的資料\n";
}

int main()
{
  fstream file = fstream("TelBook.txt", ios_base::in|ios_base::out);
  if (!file)
    cerr <<"檔案開啟失敗!!\n";
  else {
    char choice;
    do {
      cout << "請選擇功能(0)結束程式(1)輸入資料(2)搜尋資料：";
      cin >> choice;
      if (choice == '1')        // 使用者若選 1
        addone(file);
      else if (choice == '2')   // 使用者若選 2
        lookup(file);
    } while (choice != '0');
    cout << "...Goodbye...";
  }
}
