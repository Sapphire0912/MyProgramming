#include<stdio.h>
#include<stdlib.h>
main()
{
	int a;          //input
	int i,j,k,l,o;  //for
	int x=-1; 	    //output
	int odd[999];  //array
	printf("input num:");
	scanf("%d",&a);
	for(j=1;j<=a;j++)
	{
		for(i=a;i>=j;i--)
		{
			printf("   ");
		}
		for(k=1;k<j+o;k++)
		{
			odd[x]=x+=2;
			printf("%3d",odd[x]);
		}
		o++;
		printf("\n");
	}
	return 0;
}
