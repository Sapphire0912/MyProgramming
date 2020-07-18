
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
		printf("块%d计:",a);
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
		printf("案计:%d",x);
		printf("计:%d",y);
}
