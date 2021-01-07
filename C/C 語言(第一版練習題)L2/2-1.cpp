#include<stdio.h>
#include<limits.h>
#include<float.h>
main(){
	printf("char is %d bit and maximum:%d\n",CHAR_BIT,CHAR_MAX);
	printf("int minimum is:%d and maximum:%d\n",INT_MIN,INT_MAX);
	printf("long minimum is:%ld and maximum:%ld\n",LONG_MIN,LONG_MAX);
	printf("signed minimum is:%d and maximum:%d\n",SCHAR_MIN,SCHAR_MAX);
	printf("short minimum is:%d and maximum:%d\n",SHRT_MIN,SHRT_MAX);
	printf("unsigned char is maximum:%u\n",UCHAR_MAX);
	printf("unsigned int is maximum:%u\n",UINT_MAX);
	printf("unsigned long is maximum:%lu\n",ULONG_MAX);
	printf("unsigned short is maximum:%u\n",USHRT_MAX);
}
