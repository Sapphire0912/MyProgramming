#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>
#include<conio.h>
#include<string.h>
#define acc 20 //自定義變數 
#define pw 9
main()
{
	char account[acc],password[pw]; //帳號密碼空間 
	char ACC[acc]="kotori";
	char PW[pw];
	int l;
	int o,p,q,r;
	unsigned int atm=2000;  //當作銀行送你的^^ 
	int a,b,c; //迴圈,長度上限 
	int X,ATM,B,D; //副程式 
	int time=0; //鎖定時間
	printf("請註冊新的密碼:(長度8個字)");
	for(p=0;p<8;p++)
	{
		PW[p]=getch();
		putchar('*');
	}
	X:
		printf("\n若要進行交易請輸入9，否則輸入0離開\n");
		scanf("%d",&l);
		switch(l)
		{
			case 0:printf("謝謝光臨，歡迎下次再來!\n");
			   return 0;
			case 9:
			time+=10000;
			int chance=3;
	B: 
	do
	{
		printf("\n\n請輸入帳號:");
		scanf("%s",account);
		printf("請輸入密碼:");
	for(a=0;a<8;a++)
	{
		password[a]=getch();
		putchar('#');
	}
	b=strncmp(account,ACC,acc-1);
	c=strncmp(password,PW,pw-1);
	if(b==0 && c==0)
	{
		printf("\n帳號密碼正確\n");
		chance=0;  //存 提 查 定存利息 密碼變更
		unsigned int i,j,k;
		ATM:
		printf("請選擇要執行的動作:\n1.存款\t\t2.提款\n3.查詢金額\t4.密碼變更\n");
		scanf("%d",&i);
		switch(i)
		{
			case 1:printf("現在的金額為:%d\n\n",atm);
				   printf("請輸入存款的金額:");
				   scanf("%d",&j);
				   atm+=j;
				   printf("現在的金額為:%d\n",atm);
				   printf("交易完成!!若要再次使用請重新輸入帳號!否則按0離開\n\n");
				   goto X;
			case 2:printf("現在的金額為:%d\n\n",atm);
				   D:
				   printf("請輸入提款的金額:");
				   scanf("%d",&k);
				   if(k>atm)
				   {
				   		printf("輸入錯誤，請重新輸入金額:\n");
				   		goto D;
				   }
				   atm-=k;
				   printf("現在的金額為:%d\n\n",atm);
				   printf("交易完成!!若要再次使用請重新輸入帳號!否則按0離開\n\n");
				   goto X;
			case 3:printf("現在的金額為:%d\n\n",atm);
				   printf("交易完成!!若要再次使用請重新輸入帳號!否則按0離開\n\n");
				   goto X;
			case 4:printf("請輸入舊密碼:");
				   	for(a=0;a<8;a++)
					{
						password[a]=getch();
						putchar('#');
					}
				   printf("\n請輸入新密碼:(長度8個字)");
				   for(p=0;p<8;p++)
			    	{
						PW[p]=getch();
						putchar('*');
					}
					printf("\n\n修改密碼後請重新登入!\n");
					goto B;
			default:printf("輸入錯誤，請重新輸入!\n\n");
					goto ATM;
		}
	}
	else
	{
		chance--;
		printf("\n帳號密碼不正確\n");
		if(chance>0)
		{
			printf("請重新輸入\n還有%d次機會輸入\n\n",chance);
		}
		if(chance==0)
		{
		if(time>20000)
		{
			printf("已鎖定，請確認帳號密碼後再輸入!!!");
			return 0; 
		}
			printf("鎖定時間%d秒\n\n",time/1000);
			Sleep(time);
			goto X;	
		}
	}
  }while(chance>0);
	}
}

