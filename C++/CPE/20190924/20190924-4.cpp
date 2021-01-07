#include<stdio.h>
#include<stdlib.h>
using namespace std;

main(){
	int chessboard[8][8];
	int i,j,count=0;
	int king,queen,position;
	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			chessboard[i][j]=count;
			count++;
		}
	}
	
	int queen_move[16],x,y;
	int king_field[4];
	
	while(scanf("%d %d %d",&king,&queen,&position) != EOF){
		if(king==queen)
			printf("Illegal state\n");
		else{
			for(i=0;i<8;i++){
				for(j=0;j<8;j++){
					if(chessboard[i][j]==king){
						switch(j){
							case 0:
								king_field[0]=0; // upperline
								king_field[1]=chessboard[i][j+1]; // down
								break;
							case 7:
								king_field[1]=0; // lowerline
								king_field[0]=chessboard[i][j-1]; // up
								break;
							default:
								king_field[0]=chessboard[i][j-1]; // up
								king_field[1]=chessboard[i][j+1]; // down
						}
						
						switch(i){
							case 0:
								king_field[2]=0; // leftmost
								king_field[3]=chessboard[i+1][j]; // right
								break;
							case 7:
								king_field[3]=0; // rightmost
								king_field[2]=chessboard[i-1][j]; // left
								break;
							default:							
								king_field[2]=chessboard[i-1][j]; // left
								king_field[3]=chessboard[i+1][j]; // right
						}	
					}
					
					if(chessboard[i][j]==queen){
						for(x=0;x<8;x++){
							if(chessboard[i][x]!=queen)
								queen_move[x]=chessboard[i][x];		
							else
								queen_move[x]=-1;	
						}
						for(y=8;y<16;y++){
							if(chessboard[y-8][j]!=queen)
								queen_move[y]=chessboard[y-8][j];
							else
								queen_move[y]=-1;
						}
					}
				} // second for
			} // first for
			
			int debug=0,debug2=0;
			
			for(int find=0;find<16;find++){
				if(queen_move[find]==position){
					debug=0;
					for(x=0;x<4;x++){
						if(king_field[x]==position){
							debug2=0;
							printf("Move not allowed\n");
							break;					
						}
						else
							debug2=1;
						break;
					}
				}
				else
					debug=1;
			}
			if(debug2==1){
				for(x=0;x<4;x++){
					if(king_field[x]){
						printf("Continue\n");
						break;
					}
					else{
						printf("Stop\n");
						break;					
					}
				}
			}
			if(debug==1)
				printf("Illegal move\n");	
		} // else
	} // while
} // main
