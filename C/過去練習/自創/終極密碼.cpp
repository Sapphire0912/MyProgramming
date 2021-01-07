#include<stdio.h>
#include<stdlib.h>
#include<windows.h> 
#include<time.h>
int main()
{
	char c;
	int a=0; 
	int b=0; 
	int low=99,high=100;  
	int count=0;  

	srand(time(NULL)); 
	b=rand()%(high-low+1)+low;

	do 
	{	  
		printf("猜第 %d 次，請輸入 %d ～ %d 的數 ==> ",++count, low, high); 
		scanf("%d",&a);
		if(a>high)
		{
			printf("拜託別鬧!!\n");
			break;
		}
		else
		if(a<low)
		{
			printf("你難道是笨蛋嗎?!\n");
			break;
		}
		else
		if (a==b) 
			{
				printf("\t\t\t\t\tBINGO!!\n");
				break;
			}
		else
			{
				printf("\t\t\t\t\tagain!!\n"); 
				if (a>b) 
				high=a-1;  
					else 
					low=a+1;  
			}
		 
	}
	while(a!=b); 
	printf("input y or n\n");
	scanf("%c",&c);
	if(c=='y')
	{
		printf("new game start\n");
		return main();
	}
	else if (c=='n')
	{
		printf("BYE BYE !! \n");
		return 0;
	}
} 
