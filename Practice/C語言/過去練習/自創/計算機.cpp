#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{
	char b;
	float a,z,y,x,w;         	//¼Æ¦r     
	float i,j;         
	printf("input num:\n");
	scanf("%f",&a);
	do
	{
		printf("input Operation Symbol:\n");
		scanf("%s",&b);
		switch(b)
		{
			case '+':printf("input add num:\n");
					 scanf("%f",&z);
				 	a+=z;
				 	printf("num is:%f\n",a);
				 	break;
			case '-':printf("input less num:\n");
					 scanf("%f",&y);
					 a-=y;
					 printf("num is:%f\n",a);
					 break;
			case '*':printf("input multiplication num:\n");
				 	scanf("%f",&x);
					 a*=x;
					 printf("num is:%f\n",a);
					 break;
			case '/':printf("input division num:\n");
					 scanf("%f",&w);
					 a/=w;
				 	printf("num is:%f\n",a);
				 	break;
			case 'p':printf("input pow num:\n");
					 scanf("%f",&i);
					 a=pow(a,i);
					 printf("num is:%f\n",a);
					 break;
			case 's':a=sqrt(a);
					 printf("num is:%f\n",a);
					 break;
			case 'l':a=log(a);
					 printf("num is:%f\n",a);
					 break;
			case 'q':
			case 'Q':return 0;
		}
	}while(a!=0);
	return main();
}
