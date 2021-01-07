#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c;
	printf("input one num:");
	scanf("%d",&c);
	a=1;
	while(a<=c)
	{ 
		printf("*");
		a++;
		b=1;
		while(b<a-1)
		{
			b++;
			printf("*");
		}
		printf("\n");	
	}
}
