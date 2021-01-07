#include<iostream>
#include<string>
#include "Ch12-12.h"
using namespace std;

class Employee: public Person { // 員工類別
friend ostream& operator<<(ostream&, Employee &);
public:
  static int count() { return counter;}
  Employee(string n, Gender s, int a, int y):Person(n,s,a)
  {
    id = ++counter;
    seniority = y;
  }
private:
  int seniority;        // 年資
  int id;               // 員工編號
  static int counter;   // 物件計數器
};
int Employee::counter = 0;

ostream& operator<<(ostream& o, Employee & e)
{
  return o << e.id << " - " << e.name << '(' << e.age << ')'
           << " 已服務 " << e.seniority << " 年" << endl;
}

void swap(void* a, void* b)     // 交換指標用的函式
{
  void* temp = a;
  a = b;
  b = temp;
}

int main()
{                  // 建立 5 個物件
  Employee* em[5]={new Employee("李家怡", female, 28,5),
                   new Employee("楊其文", male, 37,9),
                   new Employee("陳真玉", female, 30,3),
                   new Employee("王松山", male, 55,20),
                   new Employee("張國誠", male, 47,15)};

  cout << "排序前..." << endl;
  for(int i=0;i<Employee::count();i++)   // 依序輸出各物件
    cout << *em[i];

  for(int i=0;i<Employee::count()-1;i++) // 依年齡排序物件
    for(int j=i;j<Employee::count();j++)
      if (*em[i] > *em[j])
         swap(em[i],em[j]);     // 交換指標

  cout << "排序後..." << endl;
  for(int i=0;i<Employee::count();i++)   // 輸出各物件
    cout << *em[i];
}
