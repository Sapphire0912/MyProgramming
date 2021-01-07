#include<iostream>
using namespace std;

main(){
	int value;
	int total,i;
	char choose;
	
	do{
		total=0;
		cout << "input the number: ";
		cin >> value;
		
		for(i=1;i<=value;i++){
			if(i%3==0){
				total+=i;
			}
		}
		cout << "Sum = " << total << endl;
		cin >> choose;
		
	}while(choose=='y' || choose=='Y');
	cout << "Bye!" << endl;	
}

