#include<iostream>
using namespace std;
/* 
  2. 課本p6-44 第10題 一樣必須以函式方式撰寫
*/
 
int change_money(int);
int Output(int,int,int);

main(){
	int change;
	int acceptable[4]={100,200,500,1000};
	while(1){
		cout << "換幾元的紙鈔(100,200,500,1000) : " ;
		cin >> change;
	
		for(int i=0;i<4;i++){
			if(change==acceptable[i]){
				change_money(change);
				break;
			}
			else{
				if(i==3 && acceptable[i]!=change){ 
					cout << "Error: 紙鈔面額錯誤 "
						 << endl;
						break;		
				}
			}
		}
	}
} 

int change_money(int change){
	int choose;
	int acceptable[4]={1,5,10,50};
	int number;
	
	cout << "換幾元的零錢(1,5,10,50) : ";
	cin >> choose;
	cout << "換幾個: ";
	cin >> number;
	
	for(int j=0;j<4;j++){
		if(choose==acceptable[j]){
			Output(change,choose,number);
			break;
		}
		else{
			if(j==3 && acceptable[j]!=choose){
				cout << "Error: 零錢面額錯誤 "
					 << endl;
			}
		}
	}
}

int Output(int input,int money,int quantity){
	int equal=0;
	int fifty=0,ten=0,five=0,one=0;
	equal = input-money*quantity;
	
	if(equal<0){
		cout << "Error: 換超過紙鈔的面額 "
			 << endl;
	}
	while(equal>0){
		if(equal>=50){
			equal-=50;
			fifty+=1;
		}
		if(equal>=10 && equal<50){
			equal-=10;
			ten+=1;
		}
		if(equal>=5 && equal<10){
			equal-=5;
			five+=1;
		}
		if(equal>=1 && equal<5){
			equal-=1;
			one+=1;
		}
	}
	
	if(money==50)
		fifty+=quantity;
	if(money==10)
		ten+=quantity;
	if(money==5)
		five+=quantity;
	if(money==1)
		one+=quantity;
	cout << "NT " << input << " 可換成: " 
		 << "$50: " << fifty << "個" 
		 << " $10: " << ten  << "個" 
		 << " $ 5: " << five << "個" 
		 << " $ 1: " << one  << "個" 
		 << endl << endl;  
		 return 0;
}
