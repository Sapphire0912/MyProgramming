#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
main()
{
	int a,b,d;
	char c;
	printf ("請輸入要買幾張票\n");
	scanf ("%d",&a);
	while(1)
	{
			if (a==0)
		{
			printf ("購買完畢掰掰");
			return 0;
		}
		printf ("你還要買%2d張票\n",a);
		printf ("請選擇交通工具:\n");
		printf ("1.台鐵\n");
		printf ("2.高鐵\n");
		printf ("3.飛機\n");
		c=getche();
		switch (c)
		{
			case	'1':
			case	'2':
			case	'3':
			printf ("\n請輸入要買幾張票");
			scanf ("%d",&b);
			if (b<=a)
			{
				a-=b;
				break;
			}
			else 
			{
				printf ("錯誤\n");
				break;
			}
			default:
			break;
			
		}
	}
 } 
