#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b=0;
	int i,j;
	printf("½Ð¿é¤J¼h¼Æ:");
	scanf("%d",&a);
	for(i=1;i<=a;i++)
	{
		if(i<a)
		{
			for(j=1;j<2*a;j++)
			{
				if(j==a-i+1||j==a+i-1)
				{
					b+=5;
					printf("%2d",b);
				}
				else
				printf("  ");
			}
		}
		else
		{
			for(j=1;j<2*a;j++)
			{
				b+=5;
				printf("%2d",b);				
			}
		}
		printf("\n");
	}
 } 
