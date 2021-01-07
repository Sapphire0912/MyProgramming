#include<stdio.h>
main()
{
	int name[10];
	int no,ch,en,c,sum,aver,x,y;
	
	printf("计");
	scanf("%d",&x);

    printf("腹絏");
	scanf("%d",&y);
	for(y=1;y<=x;y++)
	{	
		printf("");
		scanf("%s",&name);
	
		printf("瓣ゅ");
		scanf("%d",&ch);
	
		printf("璣ゅ");
		scanf("%d",&en);
	
		printf("祘Α");
		scanf("%d",&c);
	
	  sum=ch+en+c;
	  aver=sum/3;
	
	 printf("\t\t\tNAME:%s ",name);
	 printf("\tNO:%d \n",y);
	 printf("\t\t\t*************************\n");
	 printf("\t\t\t*\t瓣ゅ%-10d  * \n",ch);
     printf("\t\t\t*\t璣ゅ%-10d  * \n",en);
	 printf("\t\t\t*\t祘Α%-10d  * \n",c);
	 printf("\t\t\t*************************\n");
	 printf("\t\t\t*\t羆だ%-10d  * \n",sum);
	 printf("\t\t\t*\tキА%-10d  * \n",aver);
	 printf("\t\t\t*************************\n");
	
	 if (aver>79)
	 printf("\t\t\t*--单 A-- 獶盽      * \n");
	 else
	 if (aver>60)
     printf("\t\t\t*--单 B--  ぃ岿       * \n");
	 else
	 printf("\t\t\t*--单 C-- 干      * \n");
	
	 printf("\t\t\t*************************\n");
    }
	return 0;
}
