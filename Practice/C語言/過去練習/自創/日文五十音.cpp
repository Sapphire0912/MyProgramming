#include<stdio.h>
#include<stdlib.h>
main()
{
	char a;
	char x[5]={'a','i','u','e','o'}; 
	int i=0;
	printf("請輸入五十音的開頭(輸入0即可結束程式):(羅馬拼音)");
	scanf("%s",&a);
		if(a=='y')
		{
			printf("%c%c",a,x[0]);
			printf("\n\n");
			printf("%c%c",a,x[2]);
			printf("\n\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();
		}		
		if(a=='w')
		{
			printf("%c%c",a,x[0]);
			printf("\n\n\n\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();	
		}
		if(a=='n')
		{
			printf("%c",a);
			printf("\n\n\n\n");
			return main();
		}
		if(a=='t')
		{
			printf("%c%c",a,x[0]);
			printf("\n");
			printf("%s","chi");
			printf("\n");
			printf("%s","tsu");
			printf("\n");
			printf("%c%c",a,x[3]);
			printf("\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();
		}		
		if(a=='s')
		{
			printf("%c%c",a,x[0]);
			printf("\n");
			printf("%s","shi");
			printf("\n");
			printf("%c%c",a,x[2]);
			printf("\n");
			printf("%c%c",a,x[3]);
			printf("\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();			
		}
		if(a=='z')
		{
			printf("%c%c",a,x[0]);
			printf("\n");
			printf("%s","ji");
			printf("\n");
			printf("%c%c",a,x[2]);
			printf("\n");
			printf("%c%c",a,x[3]);
			printf("\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();
		}
		if(a=='d')
		{
			printf("%c%c",a,x[0]);
			printf("\n");
			printf("%s","ji");
			printf("\n");
			printf("%s","ji");
			printf("\n");
			printf("%c%c",a,x[3]);
			printf("\n");
			printf("%c%c",a,x[4]);
			printf("\n");
			return main();
		}
		switch(a)
		{
			case '0':system("pause");
					 return 0;
			default:
					do
					{
						switch(a)
						{
							case 'a':
							case 'i':
							case 'u':
							case 'e':
							case 'o':printf("%c",x[i]);
									 printf("\n");
									 break;
							default:printf("%c%c",a,x[i]);
									printf("\n");
									break;
						}
					i++;
					}while(i<5);
		}
		
	return main();
 } 
