#include<stdio.h>
#include<stdio.h>
#define MAX 1000
int getline(char line[],int maximum);
void reverse(char s[]);
main(){
	char line[MAX];
	while(getline(line,MAX)>0){
		reverse(line);
		printf("%s",line);	
	}	
	return 0;	
} 
void reverse(char s[]){
	int i,j;
	char temp;
	i=0;
	while(s[i]!='\0')
		++i;--i;
		if(s[i]=='\n')
			--i;
	j=0;
	while(j<i){
		temp=s[j];s[j]=s[i];s[i]=temp;
		--i;++j;
	}
}
int getline(char s[],int lim){
	int c,i,j;
	j=0;
	for(i=0;(c=getchar())!=EOF && c!='\n';++i)
		if(i<lim-2){
			s[j]=c;
			++j;
		}
		if(c=='\n'){
			s[j]=c;
			++j;++i;
		}
		s[j]='\0';
		return i;
}
