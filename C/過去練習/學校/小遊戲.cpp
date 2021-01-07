#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>
int main()
{
	char x;
	int a;
	printf("輸入Y進入遊戲，否則按N離開遊戲\n");
	scanf("%s",&x);
	switch(x)
	{
		case 'n':
		case 'N':printf("離開遊戲BYE BYE!!\n");
				 system("pause");
				 return 0;
		case 'y':
		case 'Y':printf("開始遊戲\n");
			   	 printf("幾條命\n");
				 scanf("%d",&a);
				 printf("%d條命 開始進入遊戲\n",a);
				 Sleep(2000);
				 printf("第一關");
				 break;
		default:printf("數值錯誤\n");
				return main();
	}
}
