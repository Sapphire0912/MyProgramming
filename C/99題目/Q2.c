#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b;
	int c=0;
	int i,j;
	int fifty=0,ten=0,five=0,one=0;
	printf("input two num:");
	scanf("%d %d",&a,&b);
	c=a-b;
	if(c>=50)
	{
		fifty++;
		c=c-50;
	}
	if(c>=10)
	{
		do{
			ten++;
			c-=10;
		}while(c>=10);
	}
	if(c>=5)
	{
		five++;
		c=c-5;
	}
	if(c>0)
	{
		do{
			one++;
			c--;
		}while(c>0);
	}
	printf("%d %d %d %d\n",fifty,ten,five,one);
	return main();
}
