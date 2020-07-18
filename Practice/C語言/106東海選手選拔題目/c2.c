#include<stdio.h>
#include<stdlib.h>
main()
{
	int a;
	int i,j;
	printf("請輸入單位:");
	scanf("%c",&i);
	switch(i)
	{
		case 'V':
		case 'v':printf("電壓,V,V,伏特\n");
				break;
		case 'A':
		case 'a':printf("電流,I,A,安培\n");
				break;
		case 'O':
		case 'o':printf("電阻,R,O,歐姆\n");
				break;
		case 'S':
		case 's':printf("電導,G,S,西門子\n");
				break;
		case 'F':
		case 'f':printf("電容,C,F,法拉\n");
				break;
		case 'H':
		case 'h':printf("電感,L,H,亨利\n");
				break;	
		case 'W':
		case 'w':printf("功率,P,W,瓦特\n");
				break;	
		case 'J':
		case 'j':printf("電能,W,J,焦耳\n");
				break;	
		case 'c':
		case 'C':printf("電量,Q,C,庫倫\n");
				break;
		default:
		return main();													
	}
}
