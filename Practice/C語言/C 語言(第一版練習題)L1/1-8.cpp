#include<stdio.h>
#include<stdlib.h>
main(){
	int c;
	int x,y,z;
	x=y=z=0;
	while((c=getchar())!=EOF){
		if(c=='\n')
		x++;
		else if(c=='\t')
			y++;
			else if(c==' ')
				z++;
				else
				break;
	}
	printf("%d %d %d\n",x,y,z);//新列 定位 空格 
} 
