#include<iostream>
#include<cstring>     // 因為用到 strcpy() 函式故含括此檔案
using namespace std;

class Person {  // 人員類別
public:
  Person(const char*, int);
  Person& operator=(Person &p);
  Person() {}
  ~Person() { delete [] name; }
  void setName(const char* ptr) { strcpy(name,ptr); }
  const char* getName() { return name;}
private:
  char* name;   // 姓名
  int age;      // 年齡
};

Person::Person(const char* s, int a)
{
  name = new char[strlen(s)];
  strcpy(name, s);
  age = a;
}

Person& Person::operator=(Person& p) // 多載指定運算子
{
  name = new char[strlen(p.name)];
  strcpy(name, p.name);
  age = p.age;
  return *this;
}

class Student : public Person {      // 學生類別繼承人員類別
public:
  void reading()
  {
    cout << id << " - " << getName() << "在看書" << endl;
  }
  Student() {}
  Student(const char* s, int a, int i) : Person(s, a)
  {                                  // 呼叫父類別的建構函式
    id = i;
  }
  Student& operator= (Student&);
private:
  int id;                            // 學號
};

Student& Student::operator= (Student& s)    // 多載指定運算子
{
  //Person::operator=(s);        // 呼叫父類別的指定運算子
  id = s.id+100;
  return *this;
}

int main()
{
  Student st1("楊其文", 10, 4), st2;
  st2 = st1;                    // 將 st1 指定給 st2
  st1.setName("李家怡");        // 更改 st1 物件的姓名
  st1.reading();
  st2.reading();
}
