# include<stdio.h>
# include<stdlib.h>

main(){
	int chess[8][8]; // 建立一個棋盤 
	int degree[8][8]; // 建立一個階層表
	int x, y;
	printf("輸入起始座標(x y): ");
	scanf("%d %d", &y, &x);
	
	int i, j;
	// 把棋盤的每個值設為0
	for(i = 0; i < 8; i++){
		for(j = 0; j < 8; j++){
			chess[i][j] = 0;
		}
	} 
	
	// 騎士的走法 8個方向 
	int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
	int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
	int count = 0;
	
	// 把階層表(每個點可以走的地方)的次數放進去
	for(i = 0; i < 8; i++){
		for(j = 0; j < 8; j++){
			for(int k = 0; k < 8; k++){
				if (i + dx[k] >= 0 && i + dx[k] <= 7){
					if (j + dy[k] >= 0 && j + dy[k] <= 7){
						count++;
					}
				}	
			}
			degree[i][j] = count;
			count = 0;
		}
	}
	
	int times;
	int xcoord[8], ycoord[8]; // 分別存放可行的x, y座標 
	
	for(times = 0; times < 64; times++){
		// 走最後一步直接跳出迴圈不用往下判斷了 
		if (chess[x][y] == 64)
			break;
		else{
			chess[x][y] = times + 1;
			degree[x][y] = 0;
		}
		
		// 先找出所有可行的路徑
		for(i = 0; i < 8; i++){
			if(x + dx[i] >= 0 && x + dx[i] <= 7){
				if (y + dy[i] >= 0 && y + dy[i] <= 7){
					xcoord[i] = x + dx[i]; // x座標 
					ycoord[i] = y + dy[i]; // y座標 
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
		
		int value[8]; // 存放階層表計算過後的值 
		int position = 0; // 紀錄位置 
		
		// 計算階層表的值 
		for(i = 0; i < 8; i++){
			if(xcoord[i] >= 0 && ycoord[i] >= 0 && degree[xcoord[i]][ycoord[i]] > 0){
				degree[xcoord[i]][ycoord[i]]--;
				value[i] = degree[xcoord[i]][ycoord[i]];
			}
			else{ 
				value[i] = 9;
			}
		}

		// 找出階層表最小值, 並找出具體位置 
		int mininum = value[0];
		for(i = 0; i < 8; i++){
			if (mininum > value[i]){
				mininum = value[i];
				position = i;
			}
		}
		
		// 最後要移動的結果
		x = xcoord[position];
		y = ycoord[position]; 
	}
	
//	 輸出結果 
	for(i = 0; i < 8; i++){
		for(j = 0; j < 8; j++){
			printf("%3d", chess[i][j]);
		}
		printf("\n");
	} 
	system("pause");
	return 0;
} 

