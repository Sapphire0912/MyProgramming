#include<stdio.h>
#include<stdlib.h>
#define MAXLINE 1000  //maximum input line size 最大輸入字串大小 
int getline(char line[],int maxline);
void copy(char to[],char from[]);
//print longest input line
main(){
	int len;  //current line length 當前字串的長度 
	int max;  // maximum length seen so far 目前為止看到的最大長度 
	char line[MAXLINE];  //current input line 當前輸入字串  
	char longest[MAXLINE]; // longest line saved here 最長的字串保存在這裡
	max=0;
	while((len=getline(line,MAXLINE))>0){
		if(len>max){
			max=len;
			copy(longest,line);
		}
		if(max>0){
			printf("Longest line is %3d character...%s\n",len,longest);			
		}
		return 0;
	} 
}
// getline:read a line into s,return length 將讀到的字串存到s[] 傳回長度 
int getline(char s[],int lim){
	int c,i;
	for(i=0;i<lim-1 && (c=getchar())!=EOF && c!='\n';++i)
		s[i]=c;
	if(c=='\n'){
		s[i]=c;
		++i;
	}
	s[i]='\0';
	return i;
} 
//copy:copy 'from' into 'to';assume 'to' is big enough 複製from[]到to[];並假設to[]足夠大
void copy(char to[],char from[]){
	int i;
	i=0;
	while((to[i]=from[i])!='\0')
		++i;
} 
