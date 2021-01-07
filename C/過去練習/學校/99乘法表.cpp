#include<stdio.h>
main()
{
	int a,b;
	for(a=1;a<10;a++)
	{
		for(b=1;b<10;b++)
		printf("%3d x %d=%3d",a,b,a*b);
		printf("\n");
	}	
	return 0;
 } 
