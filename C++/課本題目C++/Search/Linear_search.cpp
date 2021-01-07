#include<iostream>
using namespace std;

class Linear{
	public:
		int lin(int,int[]);
	private:
		int user_in;
		int length;
		int *num;
};

int Linear::lin(int number, int array[]){
	num = array;
	length = sizeof(array);
	user_in = number;
	
	for(int i=0;i<length;i++){
		if(*(num+i) == user_in)
			return true;
	}
	return false;
}

main(){
	Linear test;
	int a[6] = {3,7,8,9,30,50};
	cout << test.lin(30,a);
}
