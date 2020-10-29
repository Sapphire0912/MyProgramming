#include<stdio.h>
#include<stdlib.h>
int cf(int c,int f);
main(){
	int c,f;
	for(f=0;f<=300;f+=20){
		printf("%3d===>>%4d\n",f,cf(c,f));
	}
}
int cf(int c,int f){
	int c1,f1;
	for(f1=0;f1<=300;f1+=20){
		c1=5*(f1-32)/9;
	}
	return c1;
}


