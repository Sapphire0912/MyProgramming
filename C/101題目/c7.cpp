#include<stdio.h>
#include<stdlib.h>
int game(int,int,int,int);
main(){
	int nhp,natk,dhp,datk;
	printf("請輸入勇者.龍王(生命值 攻擊力):");
	scanf("%d %d %d %d",&nhp,&natk,&dhp,&datk);
	game(nhp,natk,dhp,datk);
	return main();
}
int game(int nh,int na,int dh,int da){
	int i=1,j;
	do{
		printf("Round %d:\n",i);
		printf("You hit Dragon %d points.\n",na);
		dh-=na;
if(dh<=0){dh=0;printf("You:%d Dragon:%d\n",nh,dh);break;}
		printf("You:%d Dragon:%d\n",nh,dh);
		printf("Dragon hits You %d points.\n",da);
		nh-=da;
if(nh<=0){nh=0; printf("You:%d Dragon:%d\n",nh,dh);break;}
		printf("You:%d Dragon:%d\n",nh,dh);
		i++;
	}while(dh>0 && nh>0);
	if(dh==0){printf("You Win!\n");}
		if(nh==0){printf("You Lose!\n");}
}
