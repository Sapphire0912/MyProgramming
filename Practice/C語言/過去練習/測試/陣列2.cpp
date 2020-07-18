#include<stdio.h>
#include<stdlib.h>
main()
{
	int c;
	int b[20];
	for(c=0;c<20;c++)
	{
		printf("Please input %d number:\n",c+1);
		scanf("%d",&b[c]);
	}
	for(c=0;c<20;c++)
	{
		if((b[c]%2==0)){
		printf("odd: %3d",b[c]);
		printf("\n");}
		else if((b[c]%2==1))
		printf("even: %3d",b[c]);
	}	
}
