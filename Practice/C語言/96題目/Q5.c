#include<stdio.h>
#include<stdlib.h>
main()
{
	int a[16][16]={{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}};
	int i,j,k;
	printf("½Ð¿é¤J¼Æ¦r:(1<=X<=15)");
	scanf("%d",&k);
	for(i=1;i<=k;i++)
	{
		for(j=1;j<=i;j++)
		{
			a[j][i]=a[j-1][i]+a[j][i-1]+a[j-1][i-1];
		}
	}
	printf("%d\n",a[k][k]);
	return main();
}
