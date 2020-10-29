#include<iostream>
using namespace std;

class Complex {
  friend ostream& operator<<(ostream&, const Complex&);
  friend istream& operator>>(istream&, Complex&);
public:
  Complex(double r=0,double i=0) {real = r; image = i;}
  Complex operator+(Complex a)    // 加法
    {return Complex(real+a.real, image+a.image);}
  Complex operator-(Complex a)    // 減法
    {return Complex(real-a.real, image-a.image);}
  bool operator==(const Complex a) // 比較
  {
    if (real == a.real && image == a.image)
      return true;
    else
      return false;
  }
private:
  double real;        // 實部
  double image;       // 虛部
};

ostream& operator<<(ostream& o, const Complex& c)
{
   return o << '(' << c.real << ',' << c.image << "i)";
}

istream& operator>>(istream& i, Complex& c)
{
  cout << "請輸入複數的實部與虛部(中間用空白隔開、不用輸入i)：";
  return i >> c.real >> c.image;
}

int main()
{
  Complex c1,c2;

  cin >> c1 >> c2; // 由鍵盤輸入兩複數的值ss
  cout << c1 << " 加 " << c2 << " 等於 " << (c1+c2) << endl;

  if (c1 == c2)    // 檢查兩複數是否相等
    cout << "您輸入的兩複數相等";
  else
    cout << "您輸入的兩複數不相等";
}
