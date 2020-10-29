#include<iostream>
using namespace std;

class Complex {
public:
  Complex(double r=0,double i=0) {real = r; image = i;}
  Complex add(Complex a)       // 猭
    {return Complex(real + a.real, image + a.image);}
  Complex minus(Complex a)     // 搭猭
    {return Complex(real - a.real, image - a.image);}
  void show()
    {cout << '(' << real << ',' << image << "i)"; }
private:
  double real;        // 龟场
  double image;       // 店场
};

int main()
{
  Complex c1,c2(3),c3(2,1);  // 篶 3 狡计ン

  c1.show();  cout << "  "; c3.show();
  cout << " 单 ";   c1.add(c3).show();

  cout << endl;

  c2.show();  cout << " 搭 "; c3.show();
  cout << " 单 ";   c2.minus(c3).show();
}
