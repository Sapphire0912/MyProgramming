#include<iostream>
#include<cstring>
using namespace std;

class Str {           
  friend int strcmp(Str&, Str&); 
public:
  void show() { cout << data; }
  void set(char * ptr) { data = ptr; }
private:
  char * data;      
};

int strcmp(Str& s1, Str& s2) 
{
  return strcmp(s1.data, s2.data);
}      

int main()
{
  Str hello, world;
  hello.set("Hello World!");
  world.set("Hello world!");
  if (strcmp(hello,world) !=0)
    cout << "The content of two strings are different." << endl;
  else
    cout << "The content of two strings are consistency." << endl;
}
