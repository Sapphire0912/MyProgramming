#include<stdio.h>
#include<stdlib.h>
main(){
	int c,x,y;
	while((c=getchar())!='\n'){
		if((c>='A' && c<='Z')||(c>='a' && c<='z')){x++;}
		else if(c>='0'&&c<='9'){x++;}
		else {x++;}
			printf("\n");
			for(y=0;y<=x;y++){printf(" ");}
			putchar(c);
	}
} 
