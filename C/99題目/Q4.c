#include<stdio.h>
#include<stdlib.h>
main()
{
	int a[4];
	int i,j;
	int x,y,z;
	printf("input four num:");
	for(i=0;i<4;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<4;i++)
		for(j=0;j<4-i;j++)
			if(a[j]<a[j+1])
			{
				x=a[j];
				a[j]=a[j+1];
				a[j+1]=x;
			}
	printf("%d-%d=%d\n",a[0],a[3],a[0]-a[3]);
	return main();
}
