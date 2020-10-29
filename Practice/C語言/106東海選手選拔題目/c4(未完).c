#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max 10
void xx(char s[]);
main()
{
	char y[max];
	int i,j,k;
	printf("進制轉換器:");
	gets(y);
	i=strlen(y);
	xx(y);
} 
void xx(char s[]){
	int i=0,j,k[max];
	while(s[i]!='\0'){
		if(s[i]>=97 && s[i]<=102){s[i]-=49;}
		i++;
		k[i]=atoi(s[i]);
		k[i]+=10;}
		for(j=0;j<=i;j++){
			printf("%d ",(int)k[j]);
		}
}
