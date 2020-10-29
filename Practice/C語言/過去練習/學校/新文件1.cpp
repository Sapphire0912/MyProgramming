#include<stdio.h>
#include<stdlib.h>
main ()
{
	int aa(void);
	int bb(void);
	int c=bb()*aa();
	printf ("%d",c);
	return 0;
 } 
 int aa(void)
 {
 	int b=4;
 	return b;
 }
 int bb(void)
 {
 	int a=6;
 	return a;
 }
