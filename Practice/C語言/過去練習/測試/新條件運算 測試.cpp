#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
main()
{
	int a,b;
	printf("input your account number:");
	scanf("%c",&a);
	do
	{
		b=getch();
		printf("*");
	}while(b!='0');
}
