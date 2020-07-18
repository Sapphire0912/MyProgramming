#include<stdio.h>
#include<stdlib.h>
main ()
{
	char oao;
	int a,b,x,y,c,d,k;
	float i;
	printf("輸入1個數字:(輸入0即可結束程式)\n");
	scanf("%d",&a);
	if(a>=60&&a<=69)
	{
		printf("請輸入1個數字，絕對值\n");
		scanf("%d",&b);
		if(b>0)
		printf("%d\n",b);
		else
		printf("%d\n",0-b);
		return main();
	}
	else
	if(a>=70&&a<=79)
	{
		printf("請輸入1個數字，8進制\n");
		scanf("%d",&c);
		printf("%o\n",c);
		return main();
	}
	else
	if(a>=80&&a<=89)
	{
		printf("輸入1個鍵，判斷大小寫\n");
		scanf("%s",&oao);
		if(oao>96)
		printf("%c 小寫\n",oao);
		if(oao<91)
		printf("%c 大寫\n",oao);
		
		return main();
	}
	else
	if(a>=90&&a<=99)
	{
		printf("輸入1個數字\n");
		scanf("%f",&i);
		printf("輸入1，C轉F；輸入2，F轉C\n");
		scanf("%d",&x);
		if(x==1)
		printf("%f\n",9*i/5+32);
		else
		if(x==2)
		printf("%f\n",((i-32)*5/9));
		return main();
	}
	else
	if(a==0) 
	{
		printf("離開程式");
		return 0;
	}
	if(a<59)
	{
		printf("輸入兩個數字(a,b)\n");
		scanf("%d,%d",&d,&y);
		printf("%d,%d\n",y,d);
		return main();
	}
	if(a>99)
	{
		printf("輸入兩個數字(a,b)\n");
		scanf("%d,%d",&d,&y);
		printf("%d,%d\n",y,d);
		return main();
	}
}
