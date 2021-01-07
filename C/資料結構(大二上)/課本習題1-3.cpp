# include<stdio.h>
# include<stdlib.h>
int F(int);
int count = 0;

main(){
	int n;
	int result;
	scanf("%d", &n);
	result = F(n);
	printf("result = %d\n", result);
	printf("count = %d\n", count);
}

int F(int n){
	count++;
	if(n == 0){
		return 0;
	}
	if(n == 1){
		return 1;
	}
	if(n == 2){
		return 2;
	}
	return F(n - 1) - F(n - 2) + F(n - 3); 
}
