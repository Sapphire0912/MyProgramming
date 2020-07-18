#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<conio.h> 
#define max 3 
int rale(void);
main(){
	int i=1,j,k,time,a,b;
	k=max*max;
	char ooxx[k],y;
	int x,re;
if(rale()==0)
	do{
re:		printf("第%d回合 輪到第%d個 player\n",i,i);Sleep(800);
		printf("請輸入要下的位置(只有兩秒的思考時間):");
		for(time=2000;time<=0;time-=2000){
			Sleep(time);
			if(time==0){
				printf("已超時，先手敗!\n");a++;i++;Sleep(800);goto re;}
			else{
				scanf("%d %c",&x,&y);}
		}	
	}while(1);
}
int rale(void){
	int x;
	printf("玩家&玩家 OOXX遊戲!\n");
	printf("1st:請輸入將要放的位置和符號(ex.第五格要劃圈圈/叉叉則請輸入:5 O/5 X)\n");
	printf("2nd:連成一條線即可獲勝!\n");
	printf("3rd:每一手只能思考兩秒鐘!\n");
	printf("4th:三戰兩勝制!\n");
	printf("瞭解上述規則後輸入0開始遊戲!\n");
	scanf("%d",&x);
	return x;
}
