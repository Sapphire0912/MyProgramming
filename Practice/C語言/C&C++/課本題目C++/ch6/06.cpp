#include<iostream>
using namespace std;
int division(int);

main(){
	int divisor;
	cout << "Enter the number: ";
	cin >> divisor;
	division(divisor);
}

int division(int d){
	int line=0;
	for(int i=1;i<=d;i++){
		if(i%13==0){
			cout << " " << i;
			line+=1;
			if(line%5==0)
				cout << endl;
		}
	}
}
