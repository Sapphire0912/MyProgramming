#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>
#define size 6
int com();
main(){
	int a[size];
	int c,i,j;
	srand(time(NULL));
printf("Dice game rule:\n");
printf("1:You have three dice.Every dice is fair and just.The number are 1 to 6.\n");
printf("2:When the game start,please throw three dice.\n");
printf("3:Play with your computer than the maximum of three dice points will add up to win.\n");
printf("4:Two wins and three wars system.\n"); 
printf("5:please input 0 to start the game.\n");
	scanf("%d",&c);
	if(c==0){
		printf("\nDice game START!!!\n");Sleep(800);
		printf("Please Waiting five second...\n");Sleep(4500);
		printf("We are preparing...\n");Sleep(800);
		printf("First round\n");Sleep(1000);
		for(i=0;i<size-3;i++){
			a[i]=(rand()%6)+1;
			printf("%2d",a[i]);
				c+=a[i];
			}
			printf("\nThe sum of your point is %d\n",c);
			com();
		}
}
int com(){
	int b[size];
	int c,i,j;
	srand(time(NULL));
	printf("\nChange the computer to throw three dice.")
}
