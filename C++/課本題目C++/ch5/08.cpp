#include<iostream>
using namespace std;

main(){
	int a;
	int i,j,k;
	cout << "Enter the number of layers: ";
	cin >> a;
	
	if(a%2==0)
		a/=2;
	if(a%2==1)
		a/=2;
		a++;
		
	for(i=1;i<=a;i++){
		for(k=1;k<=a-i;k++)
			cout << " ";
		for(j=1;j<=2*i-1;j++)
			cout << "*";
		cout << endl;
	}
	for(i=a-1;0<=i;i--){
		for(k=1;k<=a-i;k++)
			cout << " ";
		for(j=1;j<=2*i-1;j++)
			cout << "*";
		cout << "\n" ;
	}
}

