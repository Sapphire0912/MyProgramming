#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b,c,d,e;
	int t,u,v,w,x,y,z=0;
	printf("請輸入現在的時間:(24時制)(輸入方式:時 分)");
	scanf("%d %d",&a,&b);
	printf("請輸入體力(MAX):");
	scanf("%d",&c);
	printf("請輸入現在體力值為:");
	scanf("%d",&d);
	printf("請輸入幾分鐘回復:");
	scanf("%d",&e);
	t=c-d; //差t體力 
	u=t*e; //u分鐘回滿 
	v=u%60;//v分鐘 
	w=u/60;//w小時 
	x=a+w;
	y=b+v;
	if(y>=60)
	{
		y-=60;
		x++;
	}
	if(x>=24)
	{
		x-=24;
	}
	printf("體力回到最大值的時間為: %d點%d分(24時制)\n\n",x,y);
	return main();
 } 
