#include<iostream>
#include<string>
using namespace std;

enum Gender {male,female};      // 代表性別的列舉型別

class Person {  // 人員類別
public:
  Person(string, Gender, int);
  Person() {}
protected:
  string name;  // 姓名
  Gender sex;   // 性別
  int age;      // 年齡
};

Person::Person(string n, Gender s, int a) : name(n)
{
  sex = s;  age = a;
}
