#include<stdio.h>
#include<stdlib.h>
main(){
	int c,compare1,compare2;
	int x,y,z;
	int i,j,k;
	int m,n,o;
	x=y=z=0;
	while((c=getchar())!=EOF){
		if((c>='A' && c<='Z')||(c>='a' && c<='z')){
			x++;}
		else if(c>='0'&&c<='9'){
			y++;}
		else if(c=='\n'){
			break;}
		else z++;
	}
	printf("璣ゅダ:%d\n计    :%d\nㄤ才:%d\n\n璣ゅダ:",x,y,z);
	for(i=1;i<=x;i++){
		printf("=");}
		printf("%3d",x);
		printf("\n计    :");
	for(j=1;j<=y;j++){
		printf("=");}
		printf("%3d",y);
		printf("\nㄤ才:");
	for(k=1;k<=z;k++){
		printf("=");}
		printf("%3d",z);
printf("\n\n");
	compare1=(x<y)?x:y;
	compare2=(z<compare1)?z:compare1;
	for(m=1;m<=compare2;m++){
		printf("||\t\t||\t\t||\n");
	}
compare1=0;
compare2=compare1;
	compare1=(x>y)?x:y;
	compare2=(z<compare1)?z:compare1;
for(n=1;n<=compare2;n++){
	if(x==compare2 && y<compare2 && z>=compare2){
			printf("||\t\t\t\t||\n");} 
	if(x==compare2 && y>=compare2 && z<compare2){
			printf("||\t\t||\t\t\n");} 
	if(y==compare2 && x<compare2 && z>=compare2){
			printf("\t\t||\t\t||\n");}
	if(y==compare2 && x>=compare2 && z<compare2){
			printf("||\t\t||\t\t\n");}
	if(z==compare2 && y<compare2 && x>=compare2){
			printf("||\t\t\t\t||\n");}
	if(z==compare2 && y>=compare2 && x<compare2){
			printf("\t\t||\t\t||\n");}
	}

}
