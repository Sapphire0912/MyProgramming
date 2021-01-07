#include<stdio.h>
#include<stdlib.h>
main(){
	int a,c;
	int x=0;
	while((c=getchar())!=EOF){
		if(c==' '){
			++x;
			continue;}
		if(x>=1){
			printf(" ");
			x=0;}
		putchar(c);
	}
} 
