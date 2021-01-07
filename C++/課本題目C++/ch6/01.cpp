#include<iostream>
using namespace std;
int msg(int);

main(){
	int count;
	cout << "Enter line number: ";
	cin >> count;
	msg(count);
}

int msg(int a){
	for(int i=0;i<a;i++){
		cout << "HELLO C++!" << endl;
	}
}
