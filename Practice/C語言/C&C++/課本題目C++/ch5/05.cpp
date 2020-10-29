#include<iostream>
using namespace std;

main(){
	float kilogram,height;
	char sex;
	cout << "Enter your sex:(B/G) ";
	cin >> sex;
	cout << "Enter your height: ";
	cin >> height;
	
	if(sex=='B')
		kilogram = (height-80)*0.7;
	if(sex=='G')
		kilogram = (height-70)*0.6;
	
	cout << "Your standard kilogram: " << kilogram << endl; 
}
