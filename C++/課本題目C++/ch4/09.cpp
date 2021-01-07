#include<iostream>
using namespace std;

main(){
	int sum=0,s;
	for (int i=1;i<9;i++){
		s=1;
		for(int j=1;j<=i;j++){
			s*=2;
		}
		sum = sum + s;
	}
	cout << "sum: " << sum;
}
