#include<iostream>
#include<ctime>
using namespace std;
int pow(int,int);

/* CLK_TCK is Macro constant, this is included in ctime module
   expressed as the number of clocks per second.*/
   
main(){
	float start,end;
	int x,y;
	start = clock();
	cout << "Enter two numbers: pow(x,y)" ;
	cin >> x >> y;
	cout << "The answer of function is " << pow(x,y) << endl;
	end = clock();
	cout << "The program execution took a total of " 
		 << (end-start) / CLK_TCK << " seconds." ; 
	return 0;
}

int pow(int x,int y){
	if(y==1)
		return 1;
	else
		return x * pow(x,y-1);
}
