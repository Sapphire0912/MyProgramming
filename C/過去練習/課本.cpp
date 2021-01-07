#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c,d;
	c=0,d=0;
	printf("input num:\n");
	for(b=1;b<21;b++)
	{
		printf("%d num:",b);
		scanf("%d",&a);
		if((a%2)==0)
		{ 
			c++;
		}
		else if((a%2)==1)
		{
			d++;
		}
	}
	printf("偶數%d個\n",c);
	printf("奇數%d個\n",d);
	return 0;
}
