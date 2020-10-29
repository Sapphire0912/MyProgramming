#include<stdio.h>
#include<stdlib.h>
#define MAX 1000
int getline(char line[],int maxline);
void copy(char to[],char from[]);
main(){
	int len,max;
	char line[MAX],longest[MAX];
	max=0;
	while((len=getline(line,MAX))>0){
		printf("%3d:%s",len,line);
		if(len>max){
			max=len;
			copy(longest,line);
		}
	}
	if(max>0)
		printf("\nLongest line : %s\n",longest);
		getchar();
}
int getline(char s[],int lim){
	int c,i,j=0;
	for(i=0;(c=getchar())!=EOF && c!='\n';++i)
		if(i<lim-2){
			s[j]=c;
			++j;
		}
		if(c=='\n'){
			s[j]=c;
			++j;
			++i;
		}
		s[j]='\0';
		return i;		
}
void copy(char to[],char from[]){
	int i=0;
	while((to[i]=from[i])!='\0')
		++i;
}

