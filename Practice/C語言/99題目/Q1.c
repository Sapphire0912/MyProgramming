#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c,d;
	int min,hr;
	printf("input four num:");
	scanf("%d %d %d %d",&a,&b,&c,&d);
	min=(d+60)-b;
	if(min>=60)
	{
		min-=60;
	}
	else
		c--;
	hr=(c+12)-a;
	if(hr>=12)
	{
		hr-=12;
	}
	printf("%d:%d\n",hr,min);
	return main();
 } 
