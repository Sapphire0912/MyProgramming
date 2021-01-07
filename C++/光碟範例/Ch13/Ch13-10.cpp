#include<iostream>
#include<string>
#include "Ch13-10.h"    // 含括人員類別定義
using namespace std;

class Student : virtual public Person { // 學生類別
public:
  void goClass() { cout << name << "在上課" << endl; }
  Student(string n, Gender s, int a):Person(n,s,a)
  {
    id = ++counter;     // 將計數器值加 1 當成學號
  }
  Student() {id = ++counter;}
protected:
  int id;               // 學號
  static int counter;   // 物件計數器
};
int Student::counter = 0;

class Teacher : virtual public Person { // 教師類別
public:
  void goClass() { cout << name << "老師在上課" << endl;}
  Teacher(string n, Gender s, int a):Person(n,s,a)
  {
    id = ++counter;     // 將計數器值加 1 當成教師編號
  }
  Teacher() {id = ++counter;}
protected:
  int id;               // 教師編號
  static int counter;   // 物件計數器
};
int Teacher::counter = 0;

class Graduated : public Teacher, public Student { // 研究生類別
friend ostream& operator<<(ostream&, Graduated& );
public:
  Graduated(string n, Gender s, int a):Person(n,s,a) { }
                                   // 只呼叫一次 Person 的建構函式
  void goClass(bool b)
  {   // 假定以 true 表示用學生身份上課 (聽課)
    b ? Student::goClass() : Teacher::goClass();
  }
};

ostream& operator<<(ostream& o, Graduated & g)
{
  return o << g.name << "的學號：" << g.Student::id
           << ", 教師編號：" << g.Teacher::id << endl;
}

int main()
{
  Student ss[9];        // 隨意建幾個學生物件
  Teacher tt[3];        // 隨意建幾個教師物件
  Graduated g("史地分", male, 25);

  cout << g;
  g.goClass(true);
  g.goClass(false);
}
