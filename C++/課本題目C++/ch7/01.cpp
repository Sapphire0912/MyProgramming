#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int integer[10],total=0;
	for(int i=0;i<10;i++){
		cout << "Enter the number: ";
		cin >> integer[i];
		total+=pow(integer[i],2);
	}
	cout << "The sum of array is " << total << "."
		 << endl;
}
