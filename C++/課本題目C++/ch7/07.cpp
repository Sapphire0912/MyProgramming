#include<iostream>
using namespace std;

main(){
	int a=1,b=3,c=6,d=10;
	int *e=&a,*f=&b,*g=&c,*h=&d;
	cout << "Address of e,f,g,h : " << e << " " << f << " " << g << " " << h << " " << endl
		 << "Contain of e,f,g,h : " << *e << " " << *f << " " << *g << " " << *h << " " << endl;
}
