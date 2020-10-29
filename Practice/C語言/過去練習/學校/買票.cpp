#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,z; //票 
	int t;	 //交通工具 
	int b;  // 迴圈
	int S;  //副程式 
	printf("請輸入總共要購買幾張票:");
	scanf("%d",&a);
	
	for(b=1;b>0;b++)
	{
		S:
		printf("請輸入要購買幾張:\n");
		scanf("%d",&z);
		if(z>a)
		{
			printf("sorry，超過輸入張數!\n\n");
			goto S;
		}
		else
		printf("請選擇交通工具:\n");
		printf("1.台鐵\n2.高鐵\n3.飛機\n");
		scanf("%d",&t);
		switch(t)
		{
			case 1: printf("你選擇的交通工具為台鐵\n");
					a-=z;
					break;
			case 2: printf("你選擇的交通工具為高鐵\n");
					a-=z;
					break;
			case 3: printf("你選擇的交通工具為飛機\n");
					a-=z;
					break;
			default: goto S;
		}
		if(a==0)
		{
			printf("全部賣光了!\n");
			system("pause");
			return 0;
		}
		if(a<0)
		{
			printf("sorry，超過輸入張數!\n\n");
			goto S;
		}	
			printf("還可以購買%d張票\n\n",a);
	}
}
