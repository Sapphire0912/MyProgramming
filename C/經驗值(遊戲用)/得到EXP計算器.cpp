#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{
	unsigned int Lv=1,Exp,SnExp=0,Need_Exp=0;
	int x;
	printf("±o®Ï∏g≈Á≠»:");
	scanf("%d",&Exp);
	do{
		SnExp=pow(Lv,3)*10;
		if(Exp<SnExp){
			Need_Exp=SnExp-Exp;
			break;}
		if(Exp>=SnExp){
			Exp-=SnExp;
			Lv++;
			continue;}
	}while(1);
	printf("Current Lv %2d,Next Lv %2d,Need Exp %8d\n",Lv,Lv+1,Need_Exp);
	
	 return main();
}
