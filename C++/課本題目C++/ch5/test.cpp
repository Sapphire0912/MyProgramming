#include<iostream>
using namespace std;

main(){
	int value;
	int i;
	char choose;
	int user;
	
	cout << "choice:" ;
	cin >> user;
	
	switch(user){
	do{
		int total=0;
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

}

int standard(){
	char sex;
	int height;
	int kg;
	
	cout << "input your sex:(B/G) ";
	cin >> sex;
	cout << "input your height:(cm) ";
	cin >> height;
	
	if(sex=='B'){
		kg=(height-80)*0.7;
	}
	else(sex=='G'){
		kg=(height-70)*0.6;
	}
	return kg;
}
