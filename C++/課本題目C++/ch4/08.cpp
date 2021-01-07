#include<iostream>
#include<cmath>
#define PI 3.1415926
using namespace std;

main(){
	float radius;
	cout << "Calculate the sphere volume:(input radius)";
	cin >> radius;
	cout << "The sphere volume is  " << 3*PI*(int)pow(radius,3)/4;
}
