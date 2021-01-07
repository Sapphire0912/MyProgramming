#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{
	int a,b,c;
	int i,j;
	printf("input a1=");
	scanf("%d",&c);
	printf("input r=");
	scanf("%d",&b);
	printf("output n=");
	scanf("%d",&a);
	for(i=1;i<=a;i++)
	{
		j=pow(b,a)*c;
	}
	printf("input a%d=%d\n",a,j);
	return main();
}
