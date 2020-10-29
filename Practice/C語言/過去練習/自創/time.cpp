#include<stdio.h>
main()
{
	int hr,min,sec;
	int year,mon,day;
	char week[50];
	printf("註：若為凌晨0點請打00，以及請輸入2位數。(例：3點4分8秒則請輸入03:04:08)\n");
	printf("請輸入現在的時間(24小時制)：(hr:min:sec)\n");
	scanf("%d:%d:%d",&hr,&min,&sec);
	
    if(hr>23) 
    printf("！？你難道是笨蛋嗎？！＠＿＠你是過哪顆星球的時間啊？？？一天２５小時不成？！\n");
    else
    if(min>59)
    printf("！？你難道是笨蛋嗎？！＠＿＠你是看哪顆星球的時鐘啊？？？刻度多了一格是否？！\n");
    else
    if(sec>59)
    printf("！？你難道是笨蛋嗎？！＠＿＠你是看哪顆星球的秒針啊？？？電池是否太有力了？！\n");
    else
    printf("請輸入現在的日期：(year-mon-day-week)\n");
    scanf("%d-%d-%d-%s",&year,&mon,&day,&week);
    
    if(year>2017) 
    printf("！？你難道是傻子嗎？！＠＿＠幾年了都不知道？！\n");
    else
    if(mon>13)
    printf("！？你難道是白癡嗎？！＠＿＠火星人的年曆嗎？！\n");
    else
    if(day>31)
    printf("！？你難道有障礙嗎？！＠＿＠我想大概是。。。\n"); 
    else
    printf("現在的時間為：%d點 %d分 %d秒\n今天的日期為：西元 %d年 %d月 %d日 星期%s\n",hr,min,sec,year,mon,day,week);

	return 0;
 } 
