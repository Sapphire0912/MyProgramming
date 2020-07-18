#include<iostream>
using namespace std;
int comparison(int,int);

main(){
	int x,y;
	cout << "Enter two numbers: ";
	cin >> x;
	cin >> y; 
	cout << "The bogger number is " << comparison(x,y);
}

int comparison(int x,int y){
	if(x>y)
		return x;
	if(x<y)
		return y;
}
