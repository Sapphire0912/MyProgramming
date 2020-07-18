#include<iostream>
#include<string>
#include "Ch12-11.h"
using namespace std;

class Student : public Person { // 學生類別
friend ostream& operator<<(ostream&, Student &);
public:
  static int count() { return counter;}
  Student(string n, Gender s, int a):Person(n,s,a)
  {
    id = ++counter;     // 將計數器值加 1 當成學號
  }
private:
  int id;               // 學號
  static int counter;   // 物件計數器
};
int Student::counter = 0;

ostream& operator<<(ostream& o, Student & s)
{
  return o << s.id << "號：" << s.name << '/'
           << s.age << " 歲" << endl;
}

int main()
{
  Student ss[3]={Student("楊其文", male, 17),
                 Student("李家怡", female, 18),
                 Student("王松山", male, 19)};

  cout << "學生共有 " << Student::count() << " 人" << endl;
  for(int i=0;i<Student::count();i++)  // 依序輸出各物件
    cout << ss[i];
}
