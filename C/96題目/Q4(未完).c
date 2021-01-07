#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c;
	int i,j;
	int Z;
	printf("有幾個學生:");
	scanf("%d",&c);
	if(c<1 || c>10)
	{
		printf("數值錯誤\n");
		return main();
	}
	Z:	
	for(i=1;i<=c;i++)
	{
		printf("單位時間A,截止時間B.");
		scanf("%d %d",&a,&b);
		if(a<1 || b>100)
		{
			printf("請重新輸入\n");
			goto Z;
		}
	}
	
}
