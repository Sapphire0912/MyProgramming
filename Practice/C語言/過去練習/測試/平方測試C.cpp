#include<stdio.h>
#include<stdlib.h>
int exponent(int a,int x)
{
    int y = 1;
    while (x > 0) {
        y *= a;
        x--;
    }
    return y;
}
int main(void)
{
	int i;
	for (i=0;i<=12;i++){
	printf("%2d%5d\n", i, exponent(2, i));
}
    system("pause"); 
	return 0;
 } 
