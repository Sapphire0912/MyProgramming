#include<iostream>
using namespace std;

main(){
	int password,verification_pw;
	int sec_pw;
	cout << "Enter your password:(4 integer) " ;
	cin >> password;
	
	verification_pw = password;
	
	cout << "Enter your password:(4 integer) " ;
	cin >> sec_pw;
	
	if(sec_pw==verification_pw)
		cout << "success" << endl;
	else
		cout << "false" << endl;
}
