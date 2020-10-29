#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{
	int a,b,x,y;
	float c;
	printf("input sqrt of numder:");
	scanf("%d",&y);
	for(b=1;b<y;b++)
	{
		for(x=1;x<=10;x++)
		if(b==10*x+1)
		{
			printf("\n");
		}
		c=sqrt(y);
		printf("sqrt(%-3d)= %f\n",y,c);
	} 
}
