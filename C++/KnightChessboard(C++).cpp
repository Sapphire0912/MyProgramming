#include<iostream>
using namespace std;

main(){
	int chess[8][8];
	int degree[8][8];
	
	int i,j;
	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			chess[i][j] = 0;
		}
	}
	
	
	int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
	int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
	int count = 0;
	
	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			for(int k=0;k<8;k++){
				if(i + dx[k] >= 0 && i + dx[k] <= 7){
					if(j + dy[k] >= 0 && j + dy[k] <= 7){
						count++;
					}
				}
			}
			degree[i][j] = count;
			count = 0;
		}
	}
	
	int x,y;
	cout << "輸入一個座標:(x y) ";
	cin >> y >> x;
	
	int times;
	int xcoord[8], ycoord[8];
	
	for(times=0;times<64;times++){
		if (chess[x][y] == 64)
			break;
		else{
			chess[x][y] = times + 1;
			degree[x][y] = 0;
		}
		
		for(i=0;i<8;i++){
			if(x + dx[i] >= 0 && x + dx[i] <= 7){
				if(y + dy[i] >= 0 && y + dy[i] <= 7){
					xcoord[i] = x + dx[i];
					ycoord[i] = y + dy[i];
				}
				else{
					xcoord[i] = -1;
					ycoord[i] = -1;
				}
			}
			else{
				xcoord[i] = -1;
				ycoord[i] = -1;
			}
		}
		
		int value[8];
		for(i=0;i<8;i++){
			if(xcoord[i] >= 0 && ycoord[i] >= 0 && degree[xcoord[i]][ycoord[i]] > 0){
				degree[xcoord[i]][ycoord[i]]--;
				value[i] = degree[xcoord[i]][ycoord[i]];
			}
			else{
				value[i] = 9;				
			}
		}
		
		int min = value[0];
		int pos = 0;
		for(i=0;i<8;i++){
			if(min > value[i]){
				min = value[i];
				pos = i;
			}
		}
		
		x = xcoord[pos];
		y = ycoord[pos];
	}
	
	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			if(chess[i][j] < 10)
				cout << " " << chess[i][j] << " ";
			else
				cout << chess[i][j] << " ";
		}
		cout << "\n";
	}
}
