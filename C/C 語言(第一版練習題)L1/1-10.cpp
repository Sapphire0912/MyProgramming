#include<stdio.h>
#include<stdlib.h>
main(){
	int c,x=0;
	while((c=getchar())!=EOF){
		switch(c){
			case '\t':printf("\\t");
						continue;
			case '\b':printf("\\b");
						continue;
			case '\\':printf("\\");
				continue;
				default:x++;
		}
		putchar(c);
	} 
}
