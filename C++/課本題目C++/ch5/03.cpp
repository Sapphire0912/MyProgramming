#include<iostream>
using namespace std;

main(){
	int i;
	cout << "Calculate Area:(Triangle,Rectangular and Trapezoid)" << endl;
	cout << "(1,2,3):";
	cin >> i;
	
	switch(i){
		int under,height;
		int length,width;
		int upper,lower; // height was existed
		float area;
		
		case 1:
			cout << "Enter the under: ";
			cin >> under;
			cout << "Enter the height: ";
			cin >> height;
			
			area = under*height/2;
			cout << "Area is: " << area << endl;
			break;
		
		case 2:
			cout << "Enter the length: ";
			cin >> length;
			cout << "Enter the width: ";
			cin >> width;
			
			area = length*width;
			cout << "Area is: " << area << endl;
			break;
			
		case 3:
			cout << "Enter the upper: ";
			cin >> upper;
			cout << "Enter the lower: ";
			cin >> lower;
			cout << "Enter the height: ";
			cin >> height;
			
			area = (upper+lower)*height/2;
			cout << "Area is: " << area << endl;
			break;
		
		default:
			cout << "Programm Error." << endl;
			return 0;
	}
}
