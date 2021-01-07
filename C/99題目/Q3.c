#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b;
	printf("input two num:");
	scanf("%d %d",&a,&b);
	switch(a)
	{
		case 1:printf("%d\n",b*32);
		break;
		case 2:printf("%.0f\n",(float)b*0.4);
		break;
		case 3:printf("%d\n",b*4);
		break;
		case 4:printf("%d\n",b*24);
		break;
	}
	return main();
 } 
