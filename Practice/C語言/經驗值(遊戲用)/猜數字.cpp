#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<conio.h>
#include<time.h>
#define max 4
int rale(void);
int game(int [],int [],int);
int com(int [],int);
int deofdi(int),choose;
int deofdi(int choose){
start:	printf("請選擇難易度:\n");
		printf("(1)簡易模式\n");
		printf("(2)普通模式\n");
		printf("(3)困難模式\n");
		printf("(4)修羅模式\n");
		printf("(5)整人模式(˙ˇ˙)\n");
		scanf("%d",&choose);
		if(choose>5 || choose<1){
			printf("輸入錯誤，請重新輸入！\n");
			goto start;}
		else{return choose;}
}
main(){
	int a[max],i,j,m,math[max],guess,com,loop;
if(rale()==0)
	deofdi(choose);
	srand(time(NULL));
com:	
	guess=rand()%9000+1000;
	if(guess>9876 || guess<1023){printf("輸入數值錯誤！請重新輸入！\n");goto com;}
		for(i=0;i<max;i++){
			math[i]=guess%10;guess/=10;
		for(j=0;j<i;j++){
			if(math[i]==math[j]){goto com;}}}
	printf("電腦的數字為:");
		for(i=max-1;i>=0;i--){
			printf("*",i);}
loop:	
	printf("\n請輸入4個數字:\n");
	scanf("%d",&m);
	if(m>9876 || m<1023){printf("輸入數值錯誤！請重新輸入！\n");goto loop;}
		for(i=0;i<max;i++){
			a[i]=m%10;m/=10;
			for(j=0;j<i;j++){
				if(a[i]==a[j]){printf("輸入數值錯誤！請重新輸入！\n");goto loop;}}}
		printf("玩家的數字為:");
		for(i=max-1;i>=0;i--){
			printf("%d",a[i]);}
			game(math,a,choose);
// 儲存數字 
}
int rale(void){
	int x;
	printf("電腦&玩家互相猜數字!!\n");
	printf("規則:\n");
	printf("1st：請輸入4位0~9的數字(不能重複)！\n");
	printf("2nd：第一個數字不可以為0！\n");
	printf("3rd：如果猜一個數字正確位置也正確，則會顯示A；否則數字正確位置錯誤，則會顯示B！\n");
	printf("4th：如果4個數字都未猜中則會顯示C！\n");
	printf("5th：當輸入完4個數字後，電腦則會開始猜玩家的第一組數字，接著換玩家猜電腦一組數字！\n");
	printf("6th：玩到數字雙方都猜中為止，猜的組數越少則獲勝！\n");
	printf("了解上述規則輸入0即可開始遊戲！\n");
	scanf("%d",&x);
	return x;
}
//math[i] is com num; a[i] is player num
int game(int math[],int a[],int choose){
	int i=1,x,y;
	int per,p[max],c[max];
	int o=0,q=0; //o A q B
	int debug;
	Sleep(2000);
	do{
debug:	printf("\n第%d回合:\n",i);
		printf("請猜電腦的第%d組數字:",i);
		scanf("%d",&per);
		for(x=0;x<max;x++){
			p[x]=per%10;per/=10;
		for(y=0;y<x;y++){
			if(p[x]==p[y]){printf("輸入數值錯誤！請重新輸入！\n"); goto debug;}}}
				for(x=0;x<max;x++){
					for(y=0;y<max;y++){
						if(p[x]==math[y]){
							if(x==y){o++;}
							else if(x!=y){q++;}}}}
			printf("%dA%dB\n",o,q);i++;
			if(o==4){printf("恭喜答對了！總共花了%d組猜中！",i-1);break;}
			else{o=0;q=0;}
		}while(1);
}// 玩家猜電腦  

