#include<iostream>
using namespace std;
int recursion(int);

main(){
	cout << "1+2+3+...+100 = " << recursion(100);
}

int recursion(int x){
	if(x<=1)
		return 1;
	else
		return x + recursion(x-1);
}
