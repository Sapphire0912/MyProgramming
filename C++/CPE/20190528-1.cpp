#include<stdio.h>
#include<stdlib.h> 
#include<math.h>

main(){
	int count,number,minus;
	int x,y,z,i,j=0;
	int c[40];
	scanf("%d",&count);
	int ans[count];
	for(x=0;x<count;x++){
		scanf("%d",&number);
		for(y=0;y<number;y++)
			scanf("%d",&c[y]);
		for(z=0;z<1000;z++){
			for(i=0,minus=c[0];i<number-1;i++)
				c[i]=abs(c[i]-c[i+1]);
			c[i]=abs(c[i]-minus);
		}
		for(i=0,ans[x]=0;i<number;i++){
			if(c[i]!=0){
				ans[x]=1;
				break;
			}	
		}
	}
	for(x=0;x<count;x++){
		if(ans[x]==0)
			printf("ZERO\n");
		else
			printf("LOOP\n");
	}
}
