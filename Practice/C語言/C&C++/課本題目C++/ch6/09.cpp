#include<iostream>
using namespace std;
int maximum_common_factor(int,int);

main(){
	int number,number2;
	cout << "Calculate maximum common factor: ";
	cin >> number >> number2;
	cout << "The maximum common factor of " 
		 << number << "," << number2 << " is " 
		 << maximum_common_factor(number,number2)
		 << endl;
}

int maximum_common_factor(int x,int y){
	int com_factor,t;
	if(x>y)
		t=y;
	else
		t=x;
	
	for(int i=1;i<=t;i++){
		if(x%i==0){
			if(y%i==0)
				com_factor=i;
		}
	}
	return com_factor;
}
