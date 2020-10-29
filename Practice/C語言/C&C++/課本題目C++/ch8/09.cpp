#include<iostream>
using namespace std;

class Complex {
public:
  void set(double r,double i) {real = r; image = i;}
  void show()
      { cout << '(' << real << ',' << image << "i)"; }
 	Complex& add(Complex a)       
      {real += a.real; image += a.image; return *this;}
      
	Complex& minus(Complex a)    
      {real -= a.real; image -= a.image; return *this;}
      
	Complex& times(Complex a);
	Complex& divide(Complex a);
private:
  double real;        
  double image;       
};

Complex& Complex::times(Complex a){
	double R = real*a.real-image*a.image;
	double I = real*a.image+image*a.real;
	real = R;
	image = I;
	return *this;
}

Complex& Complex::divide(Complex a){  //ac+bd bc-ad <i /c^2+d^2
	double R = (real*a.real+image*a.image) / (a.real*a.real+a.image*a.image);
	double I = (image*a.real-real*a.image) / (a.real*a.real+a.image*a.image);
	real = R;
	image = I;
	return *this;
}

int main()
{
  Complex c1,c2;
  c1.set(3, 9);
  c2.set(-1, 2.5);

  c1.show();  cout << " add "; c2.show();
  cout << " Equal: ";   c1.add(c2).show();
  cout << endl;
  
  c2.show();  cout << " minus "; c1.show();
  cout << " Equal: ";   c2.minus(c1).show();
  cout << endl;
  
  c1.show();  cout << " times "; c2.show();
  cout << " Equal: ";   c1.times(c2).show();
  cout << endl;
  
  c1.show();  cout << " divide by "; c2.show();
  cout << " Equal: ";   c1.divide(c2).show();
  cout << endl;
}
