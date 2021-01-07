#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>
#include<windows.h>
#include<time.h>
main()
{
	printf("猜數字!!\n");
	printf("規則:\n");
	printf("1st：請輸入4位0~9的數字(不能重複)！\n");
	printf("2nd：第一個數字不可以為0！\n");
	printf("3rd：如果猜一個數字正確位置也正確，則會顯示A；否則數字正確位置錯誤，則會顯示B！\n");
	printf("4th：如果4個數字都未猜中則會顯示C！\n");
	printf("閱讀完上述規則即可開始遊戲！\n");
	
	char x;
	int a,b,c,d;
	int i,j,k,l;
	int m;
	int q,w,e,r;
	q=a;
	w=b;
	e=c;
	r=d;
	q=getchar();
	printf("\n請輸入四個數字：(x.x.x.x)");
	scanf("%d.%d.%d.%d",&q,&w,&e,&r);

		printf("\n是否要更改數字？(y/n)\n");
		scanf("%s",&x);
	
		if(x=='y')
		{
			printf("\n");
			return main();
		}
		else if(x=='n')
		{
			printf("%d%d%d%d",a,b,c,d);
			Sleep(500);
			printf("\t\t\b\b\b\b");
			printf("\n開始遊戲吧！\n");
			for(m=1;m>0;m++)
			{
				printf("請猜第%d組數字：(x.x.x.x)",m);
				scanf("%d.%d.%d.%d",&i,&j,&k,&l);
				if(a==i && b==j && c==k && d==l)
				{
					printf("\t\t\t      4A  ");
					printf("恭喜猜對了！！！\n");
					return 0;
				}
				else if(a==i && b==j && c==k && d!=l)
				{
					 printf("\t\t\t      3A  ");
					 printf("\n");
				}
				else if(a==i && b==j && c!=k && d==l)
				{
					printf("\t\t\t      3A  ");
					printf("\n");
				}
				else if(a==i && b!=j && c==k && d==l)
				{
					printf("\t\t\t      3A  ");
					printf("\n");
				}
				else if(a!=i && b==j && c==k && d==l)
				{
					printf("\t\t\t      3A  ");
					printf("\n");
				}
				else if(a==i && b==j && c!=k && d!=l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a==i && b!=j && c==k && d!=l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a!=i && b==j && c==k && d!=l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a==i && b!=j && c!=k && d==l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a!=i && b==j && c!=k && d==l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a!=i && b!=j && c==k && d==l)
				{
					printf("\t\t\t      2A  ");
					printf("\n");
				}
				else if(a!=i && b!=j && c!=k && d==l)
				{
					printf("\t\t\t      1A  ");
					printf("\n");
				}
				else if(a!=i && b!=j && c==k && d!=l)
				{
					printf("\t\t\t      1A  ");
					printf("\n");
				}
				else if(a!=i && b==j && c!=k && d!=l)
				{
					printf("\t\t\t      1A  ");
					printf("\n");
				}
				else if(a==i && b!=j && c!=k && d!=l)
				{
					printf("\t\t\t      1A  ");
					printf("\n");
				}
			}
		}
		return 0;
}
