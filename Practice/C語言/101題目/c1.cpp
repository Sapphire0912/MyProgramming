#include<stdio.h>
#include<stdlib.h>
int day(int,int);
main(){
	int y,m;
	printf("請輸入年份(民國)和月份格式(ex.90年8月 輸入90 8)\n");
	scanf("%d %d",&y,&m);
	if((y>=0 || y<=150) && (m>=1 || m<=12)){
		printf("%d\n",day(y,m));
		return main();}
		else
		return main();
} 
int day(int year,int month){
	if(year<90 || (year==90 && month<8) && year>101 || (year==101 && month>7)){	
		month=0;}
	else{
	year-=90;year*=12;month=year-7+month;}
		return month;
}
