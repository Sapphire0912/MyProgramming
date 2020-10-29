#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{ 
	int c;
	float a,b;
	printf("output b is sqrt\n");
	printf("input one number:(X.XXXXXX)");
	scanf("%f",&b);
	a=pow(b,2);
	c=a+0.5;
	if(b<1.0)
	{
		printf("給我滾!!!不要找程式語言麻煩!!");
		return 0;
	}
	else if(b>=1.0) 
	{
		printf("%f=b%d",b,c);
		printf("\n");
	}
	return main();
}
