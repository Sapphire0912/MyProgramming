#include<iostream>
using namespace std;

void overload(char x,char y){
	cout << "x and y are char: " << x << " and "<< y;
}

void overload(char x,int y){
	for(int i=0;i<y;i++){
		cout << x;
	}
}

void overload(int x,char y){
	for(int i=0;i<x;i++){
		cout << y;
	}
}

void overload(int x,int y){
	cout << "x times y equal " << x*y;
}


main(){
	overload('A','B');
}
