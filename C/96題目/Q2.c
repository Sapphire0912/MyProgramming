#include<stdio.h>
#include<stdlib.h>
main()
{
	int a,b;
	printf("今年2007年,請輸入月.日");  //2007.8.1 三 
	scanf("%d %d",&a,&b);
	if(a<1 || a>12 || b<1 || b>31)
	{
		printf("請重新輸入\n");
		return main();
	}
	if(a==2 && b>28 || a==4 && b>30 || a==6 && b>30 || a==9 && b>30 || a==11 && b>30 )
	{
		printf("請重新輸入\n");
		return main();
	 } 
	switch(a)
	{
		case 1:
				if((b-1)%7==0)
					printf("月\n");
				if((b-1)%7==1)
					printf("火\n");	
				if((b-1)%7==2)
					printf("水\n");
				if((b-1)%7==3)
					printf("木\n");	
				if((b-1)%7==4)
					printf("金\n");	
				if((b-1)%7==5)
					printf("土\n");
				if((b-1)%7==6)
					printf("日\n");						
				break;
		case 2:
		case 3:
				if((b-1)%7==0)
					printf("木\n");
				if((b-1)%7==1)
					printf("金\n");	
				if((b-1)%7==2)
					printf("土\n");
				if((b-1)%7==3)
					printf("日\n");	
				if((b-1)%7==4)
					printf("月\n");	
				if((b-1)%7==5)
					printf("火\n");
				if((b-1)%7==6)
					printf("水\n");						
				break;	
		case 4:
				if((b-1)%7==0)
					printf("日\n");
				if((b-1)%7==1)
					printf("月\n");	
				if((b-1)%7==2)
					printf("火\n");
				if((b-1)%7==3)
					printf("水\n");	
				if((b-1)%7==4)
					printf("木\n");	
				if((b-1)%7==5)
					printf("金\n");
				if((b-1)%7==6)
					printf("土\n");						
				break;
		case 5:
				if((b-1)%7==0)
					printf("火\n");
				if((b-1)%7==1)
					printf("水\n");	
				if((b-1)%7==2)
					printf("木\n");
				if((b-1)%7==3)
					printf("金\n");	
				if((b-1)%7==4)
					printf("土\n");	
				if((b-1)%7==5)
					printf("日\n");
				if((b-1)%7==6)
					printf("月\n");						
				break;	
		case 6:
				if((b-1)%7==0)
					printf("金\n");
				if((b-1)%7==1)
					printf("土\n");	
				if((b-1)%7==2)
					printf("日\n");
				if((b-1)%7==3)
					printf("月\n");	
				if((b-1)%7==4)
					printf("火\n");	
				if((b-1)%7==5)
					printf("水\n");
				if((b-1)%7==6)
					printf("木\n");						
				break;
		case 7:
				if((b-1)%7==0)
					printf("日\n");
				if((b-1)%7==1)
					printf("月\n");	
				if((b-1)%7==2)
					printf("火\n");
				if((b-1)%7==3)
					printf("水\n");	
				if((b-1)%7==4)
					printf("木\n");	
				if((b-1)%7==5)
					printf("金\n");
				if((b-1)%7==6)
					printf("土\n");						
				break;
		case 8:
				if((b-1)%7==0)
					printf("水\n");
				if((b-1)%7==1)
					printf("木\n");	
				if((b-1)%7==2)
					printf("金\n");
				if((b-1)%7==3)
					printf("土\n");	
				if((b-1)%7==4)
					printf("日\n");	
				if((b-1)%7==5)
					printf("月\n");
				if((b-1)%7==6)
					printf("火\n");						
				break;	
		case 9:
				if((b-1)%7==0)
					printf("土\n");
				if((b-1)%7==1)
					printf("日\n");	
				if((b-1)%7==2)
					printf("月\n");
				if((b-1)%7==3)
					printf("火\n");	
				if((b-1)%7==4)
					printf("水\n");	
				if((b-1)%7==5)
					printf("木\n");
				if((b-1)%7==6)
					printf("金\n");						
				break;	
		case 10:
				if((b-1)%7==0)
					printf("月\n");
				if((b-1)%7==1)
					printf("火\n");	
				if((b-1)%7==2)
					printf("水\n");
				if((b-1)%7==3)
					printf("木\n");	
				if((b-1)%7==4)
					printf("金\n");	
				if((b-1)%7==5)
					printf("土\n");
				if((b-1)%7==6)
					printf("日\n");						
				break;
		case 11:
				if((b-1)%7==0)
					printf("木\n");
				if((b-1)%7==1)
					printf("金\n");	
				if((b-1)%7==2)
					printf("土\n");
				if((b-1)%7==3)
					printf("日\n");	
				if((b-1)%7==4)
					printf("月\n");	
				if((b-1)%7==5)
					printf("火\n");
				if((b-1)%7==6)
					printf("水\n");						
				break;
		case 12:
				if((b-1)%7==0)
					printf("土\n");
				if((b-1)%7==1)
					printf("日\n");	
				if((b-1)%7==2)
					printf("月\n");
				if((b-1)%7==3)
					printf("火\n");	
				if((b-1)%7==4)
					printf("水\n");	
				if((b-1)%7==5)
					printf("木\n");
				if((b-1)%7==6)
					printf("金\n");						
				break;																				
	 } 
	 return main();
}
