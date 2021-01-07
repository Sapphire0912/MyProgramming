#include<iostream>
using namespace std;

main(){
	int i=5;
	int *j=&i;
	cout << "pointer: " << j << endl
		 << "value: " << *j ;
}
