#include<iostream>
using namespace std;

main(){
	int array[5]={2,3,4,5,6};
	int *ptr = array;
	for(int i=0;i<5;i++){
		cout << "Value of array is " << *(ptr+i)
			 << endl;
	}
}
