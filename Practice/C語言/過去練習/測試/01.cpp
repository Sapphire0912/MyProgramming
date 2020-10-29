#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a=1,b=1,c=a++,d=++b;
	printf("%d %d %d %d",a,b,c,d);
	system("pause");
	return 0;
}
