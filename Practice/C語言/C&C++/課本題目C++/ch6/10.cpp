#include<iostream>
using namespace std;
int change_money(int);
int Output(int,int,int);

main(){
	int change;
	int acceptable[4]={100,200,500,1000};
	cout << "Change for change:(Only accept banknotes) "
		 << "NT (100,200,500,1000)" ;
	cin >> change;
	for(int i=0;i<4;i++){
		if(change==acceptable[i]){
			change_money(change);
			break;
		}
		else{
			if(i==3 && acceptable[i]!=change){ 
				cout << "Error: Enter the wrong denomination. "
					 << endl;		
			}
		}
	}
} 

int change_money(int change){
	int choose;
	int acceptable[4]={1,5,10,50};
	int number;
	cout << "Change for change(1,5,10,50)";
	cin >> choose;
	cout << "Enter the number of change:";
	cin >> number;
	for(int j=0;j<4;j++){
		if(choose==acceptable[j]){
			Output(change,choose,number);
			break;
		}
		else{
			if(j==3 && acceptable[j]!=choose){
				cout << "Error: Enter the wrong denomination."
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
		cout << "Error: Out of denomination."
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
	cout << "NT " << input << " -->> " 
		 << "$50: " << fifty 
		 << " $10: " << ten
		 << " $ 5: " << five
		 << " $ 1: " << one
		 << endl;  
		 return 0;
}
