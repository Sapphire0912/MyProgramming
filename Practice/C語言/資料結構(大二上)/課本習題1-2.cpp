# include<stdio.h> 
# include<stdlib.h>
int Fib(int);

main(){
	int n, result;
	scanf("%d", &n);
//	result = Fib(n);
//	printf("result = %d\n", result);

	int last = 0, next = 1, total = 0;
	for(int loop = 2; loop <= n; loop++){
		total = last + next;
		last = next;
		next = total;
	}
	printf("total = %d\n", total);
} 

int Fib(int n){
	if(n == 0)
		return 0;
	if(n == 1)
		return 1;
	return Fib(n - 1) + Fib(n - 2);
}
