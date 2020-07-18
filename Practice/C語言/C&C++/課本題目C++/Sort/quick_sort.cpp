#include<iostream>
using namespace std;

void quick(int *sort,int len){
	int key_value[len],left[len],right[len];
}

main(){
	int list[7] = {20, 9, 55, 11, 7, 90, 33};
	int *num = list;
	
	cout << "Original: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
	quick(num,sizeof(list)/4);
	
	cout << "Sorted: ";
	for(int i=0;i<sizeof(list)/4;i++)
		cout << *(num+i) << " ";
	cout << endl;
}
}
