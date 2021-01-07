#include<iostream>
using namespace std;
int sum(int);

main(){
	int n;
	cout << "Enter the n: ";
	cin >> n;
	cout << "1+2+3+...+n = " << sum(n); 
}

int sum(int n){
	if(n==1)
		return 1;
	else
		return n + sum(n-1);
} 
