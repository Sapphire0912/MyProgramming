#include<iostream>
#define pw 6127
using namespace std;

main(){
	int user_input;
	cout << "Enter four number:(1 to 9) ";
	cin >> user_input;
	
	if(user_input==pw)
		cout << "Winning" << endl;
	else
		cout << "Didn't win" << endl;
}
