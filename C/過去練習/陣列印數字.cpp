
#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,i;
	int x=0,y=0;
	int even[22];
	int odd[22];
	for(a=1;a<21;a++)
	{
		printf("輸入%d個數:",a);
		scanf("%d",&i);
		if((even[i]%2)==0)
		{
			x=x+even[i];
		}
		else if((odd[i]%2)==1)
		{
			y=y+odd[i];
		}
	}
		printf("偶數:%d",x);
		printf("奇數:%d",y);
}
