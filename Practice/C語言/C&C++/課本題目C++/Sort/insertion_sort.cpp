#include<iostream>
using namespace std;

void insert(int *sort,int len){
	int temp,j;
	for(int i=1;i<len;i++){
		temp = *(sort+i);
		j = i - 1;
		while(j>=0 && temp < *(sort+j)){
			*(sort+j+1) = *(sort+j);
			j--;
		}
		*(sort+j+1) = temp;
	}
}

main(){
	int list[7] = {20, 9, 55, 11, 7, 90, 33};
	int *num = list;
	
	cout << "Original: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
	insert(num,sizeof(list)/4);
	
	cout << "Sorted: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
}
