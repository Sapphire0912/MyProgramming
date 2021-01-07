#include<iostream>
using namespace std;
float sum(int);

main(){
	int n;
	cout << "Enter the n: ";
	cin >> n;
	cout << "1/1+1/2+1/3+...+1/n = " << sum(n); 
}

float sum(int n){
	float total=0;
	for(float i=1;i<=n;i++){
		total+=(1/i);
	}
	return total;
}
