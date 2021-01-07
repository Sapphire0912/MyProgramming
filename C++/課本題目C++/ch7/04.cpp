#include<iostream>
using namespace std;

main(){
	char password[6]={'e','x','0','9','1','2'};
	char keyboard[6];
	int i,j,jump=0;
	int chance=3;
	while(chance>0){
		chance--;
		cout << "Enter the password: " ;
		for(i=0;i<6;i++){
			cin >> keyboard[i];
		}
		for(j=0;j<6;j++){
			if(keyboard[j]==password[j]){
				if(j==5){
					cout << "Logic successful." << endl;
					jump=1;
				}
				else
					continue;
			}
			else{
				cout << "Password is error.You will " << chance << " chance left."
					 << endl;
				break;
			}
		}
		if(chance<=0)
			cout << "Logic failed." << endl;
		if(jump==1)
			break;
	}
}	
