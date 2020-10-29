#include<iostream>
#include<string>
using namespace std;

int main()
{
  string s1 = "wonderful";
  string s2 = "wonder";
  cout << s1.compare("Wonderful") << endl;
  cout << s1.compare(3,4,"door") << endl;
  cout << s1.compare(0,6,s2) << endl;
}
