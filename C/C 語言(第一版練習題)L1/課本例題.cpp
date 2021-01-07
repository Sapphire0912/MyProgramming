#include<stdio.h>
#include<stdlib.h>
int power(int m,int n);
main(){
	int x;
	for(x=0;x<10;x++){
		printf("%d %d %d\n",x,power(2,x),power(3,x));
	}
	return 0;
} 
int power(int i,int j){
	int a,b=1;
	for(a=1;a<=j;a++){
		b=b*i;
	}
	return b;
}
