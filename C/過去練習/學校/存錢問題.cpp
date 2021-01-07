#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c,d;
	printf("請輸入存款:\n");
	scanf("%d",&d);
	while(d>=0)
	{
		printf("請輸入(1)加(2)減:");
		scanf("%d",&c);
		switch(c)
		{
			case 1:
				printf("請輸入加多少:\n");
				scanf("%d",&b);
				d+=b;
				printf("現在的金額為:%d\n",d);
				break;
			case 2:
				printf("請輸入減多少:\n");
				scanf("%d",&a);
				d-=a;
				printf("現在的金額為:%d\n",d);
				break;
			default:
				printf("輸入錯誤 重新輸入\n");
				return main();
		}
	}
	printf("金額不足請先加錢!\n");
	system("pause\n");
	return 0;
 } 
