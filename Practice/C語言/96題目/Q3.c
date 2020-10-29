#include<stdio.h>
#include<stdlib.h>
main()//ぃ穦Τや计  ぃ穦Τ程挡狦ㄢ囊布计单 
{
	int c,a,b;
	int i,j=0,k=0;
	int x=0,y=0;
	printf("块碭:");
	scanf("%d",&i);
	for(c=1;c<=i;c++)
	{
		printf("块A B囊や计:"); 
		scanf("%d %d",&a,&b);
		if(a>b)
		{
			j=a+b;
			x+=j;		
		}
		if(a<b)
		{
			k=a+b;
			y+=k;
		}
	 } 
	if(x>y)
	{
		printf("A %d\n",x-y);
	}
	else if(x<y)
	{
		printf("B %d\n",y-x);
	}
	return main();
}
