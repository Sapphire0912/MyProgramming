#include<iostream>
#include<cmath>
using namespace std;

const float a = 3.14159f;
int main ()
{
	float x, y;
	float z = 5;
	x = a* float (pow(z, 2)) ;
	y =2*a*z;
	cout <<"¶ê­±¿n1 =" << x
	     <<"\t¶ê©Pªø1 ="<< y;
    z = 10;
	x = a*float (pow(z,2));
	y =2*a*z;
	cout <<"\n¶ê­±¿n2 =" << x
	     <<"\t¶ê©Pªø2 =" << y << endl;
	system("pause");
	return 0;
}
