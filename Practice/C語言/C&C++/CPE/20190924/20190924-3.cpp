#include<stdio.h>
#include<stdlib.h>

main(){
	int card[5][5],count;
	int i,j;
	int x;
	int a,b;
	int number[75];
	
	scanf("%d",&count);
	while(count>0){
		count--;
		for(i=0;i<5;i++){
			for(j=0;j<5;j++){
				if(i==2 && j==2){
					card[i][j]=0;
				}
				else
					scanf("%d",&card[i][j]);
			}
		}
	    for(i=0;i<15;i++){
	    	scanf("%d",&number[i]);
		}
		for(i=0;i<5;i++){
			for(j=0;j<5;j++){
				for(x=0;x<15;x++){
					if(number[x]==card[i][j]){
						card[i][j]=0;
						for(a=0;a<5;a++){
//						if(card[a][0]==card[a][1] && card[a][1]==card[a][2] && card[a][2]==card[a][3] && card[a][3]==card[a][4] && card[a][4]==0){
//							printf("BINGO after %d numbers announced\n",x+1);
//							break;
//						}
//			
//						if(card[0][a]==card[1][a] && card[1][a]==card[2][a] && card[2][a]==card[3][a] && card[3][a]==card[4][a] && card[4][a]==0){
//							printf("BINGO after %d numbers announced\n",x+1);
//							break;
//						}
//
//						if(card[0][0]==card[1][1] && card[1][1]==card[2][2] && card[2][2]==card[3][3] && card[3][3]==card[4][4] && card[4][4]==0){
//							printf("BINGO after %d numbers announced\n",x+1);
//							break;
//						}
//						
//						if(card[0][4]==card[1][3] && card[1][3]==card[2][2] && card[2][2]==card[3][1] && card[3][1]==card[4][0] && card[4][0]==0){
//							printf("BINGO after %d numbers announced\n",x+1);
//							break;
//						}
//						
						}
					}	
				}
			}
		}
	}
}

