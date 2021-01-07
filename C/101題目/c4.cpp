#include<stdio.h>
#include<stdlib.h>
main(){
	int num,a[8],i,j,sum=0;
	int x;
	printf("請輸入學號(7碼):");
	scanf("%d",&num);
	for(i=1;i<8;i++){
		a[i]=num%10;num/=10;}
		for(j=7,i=1;j>=1,i<8;j--,i++){
			a[i]*=j;
			sum+=a[i];}
		if(sum%10!=0){
			sum%=10;
			x=10-sum;
			printf("%d\n",x);}
			else
			 printf("0\n");
			 return main();
}
