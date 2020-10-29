#include<stdio.h>
#include<math.h>
main()
{
	int a=2,b,c;

	for(b=1;b<11;b++)
	{
	 c=pow(a,b);
	printf("%d^%2d=%3d\n",a,b,c);
	}
	return 0;
}
