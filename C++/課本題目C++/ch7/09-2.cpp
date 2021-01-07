#include<iostream>
using namespace std;
int sum(int*,int*);
int maximum(int*,int*);
int *sorted(int*,int*);

int main(){
	int array[]={45,65,24,49,68,78,45,12,32,40};
	int size=sizeof(array)/4;
	int total,max,*sort;
	total=sum(array,&size);
	max=maximum(array,&size);
	sort=sorted(array,&size);
	cout << "Sum : " << total << endl
		 << "Max : " << max   << endl
		 << "Sorted : ";
	for(int i=0;i<size;i++){
		cout << *(sort+i) << " " ;
	}
	cout << endl;
} 

int sum(int *array,int *len){
	int total=0;
	for(int i=0;i<*len;i++){
		total+=*(array+i);
	}
	return total;
}

int maximum(int *array,int *len){
	int temp=*(array);
	for(int i=0;i<*len-1;i++){
		if(temp<*(array+i)){
			temp=*(array+i);
		}
	}
	return temp;
}

int *sorted(int *array,int *len){
	int i,j,temp;
	for(i=0;i<*len;i++){
		for(j=0;j<*len;j++){
			if(*(array+j)>*(array+j+1)){
				temp=*(array+j);
				*(array+j)=*(array+j+1);
				*(array+j+1)=temp;
			}
		}
	}
	return array;
}
