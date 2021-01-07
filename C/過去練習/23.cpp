#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
main()
{
	int a[6],b[20],c,f,g;   //a帳號 b密碼 c模式切換 
	char d,e;
	printf("\n");
	printf("\n輸入使用者帳號:");
	scanf("%s",&a[d]);
	printf("\n輸入使用者密碼:");
    scanf("%s",&b[d]);

    printf("-----------------------");
{	
    printf("\n\n註冊完成!!");
    printf("\n\n您的使用者帳號為:%s",a);
	printf("\n\n您的使用者密碼為:%s",b);
 } 
 {

 S:
 printf("\n\n請選擇您要的遊玩模式~~");
 printf("\n(1)一般模式 \n(2)故事模式 \n(3)夢魘模式 \n(4)無敵模式");
 printf("\n我要第  ",g);
 scanf("%d",&g);}
if(g<1||g>4) 
{
 printf("\n請別開玩笑");
 goto S;
}
 switch(g)

 { 	
{
case 1:printf("你選擇了 一般模式\n");
break;
case 2:printf("你選擇了 故事模式\n");
break;
case 3:printf("你選擇了 夢魘模式\n");
break;
case 4:printf("你選擇了 無敵模式\n");
break;  	

 	
 }

 
 }

	
	
	
	return main();
	}
