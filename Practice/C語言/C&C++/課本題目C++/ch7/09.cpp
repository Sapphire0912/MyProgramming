#include<iostream>
using namespace std;
int sum(int[],int);
int maximum(int[],int);
int sorted(int[],int);

int main(){
	int array[]={45,65,24,49,68,78,45,12,32,40};
	int total,max;
	total=sum(array,10);
	max=maximum(array,10);
	sorted(array,10);
	cout << "Sum : " << total << endl
		 << "Maximum : " << max << endl;
}

int sum(int array[],int len){
	int add=0;
	for(int i=0;i<len;i++){
		add+=array[i];
	}
	return add;
}

int maximum(int array[],int len){
	int num;
	num=array[0];
	for(int i=0;i<len-1;i++){
		if(num<array[i+1])
			num=array[i+1];
	}
	return num;
}

int sorted(int array[],int len){
	int temp,i,j;
	for(i=0;i<len;i++){
		for(j=0;j<len;j++){
			if(array[j]>array[j+1]){
				temp=array[j];
				array[j]=array[j+1];
				array[j+1]=temp;
			}
		}
	}
	cout << "Sorted : ";
	for(int i=0;i<10;i++){
		cout << array[i] << " ";
	}
	cout << endl;
}
