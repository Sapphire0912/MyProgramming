#include<iostream>
using namespace std;

main(){
	int a=10,b=20,c=30;
	int temp;
	cout << "交換前 a = " << a
		 << " b = " << b
		 << " c = " << c
		 << endl ;
	temp=a;
	a=c;
	c=b;
	b=temp;
	cout << "交換後 a = " << a
		 << " b = " << b
		 << " c = " << c
		 << endl ;	
}
