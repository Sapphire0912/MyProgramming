#include<iostream>
using namespace std;

void bubble(int *sort,int len){
	int temp;
	for(int i=0;i<len;i++){
		for(int j=0;j<i;j++){
			if(*(sort+i) < *(sort+j)){
				temp = *(sort+i);
				*(sort+i) = *(sort+j);
				*(sort+j) = temp;
			}
		}
	}
}

main(){
	int list[7] = {20, 9, 55, 11, 7, 90, 33};
	int *num = list;
	
	cout << "Original: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
	bubble(num,sizeof(list)/4);
	
	cout << "Sorted: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
} 
