#include<iostream>
using namespace std;

main(){
	int cost=137;
	int fifty=50,ten=10,five=5,one=1;
	int count_50=0,count_10=0,count_5=0,count_1=0;
	
	while(cost!=0){
		if(cost>=50){
			cost-=50;
			count_50+=1;
			continue;
		}
		if(cost>=10){
			cost-=10;
			count_10+=1;
			continue;
		}
		if(cost>=5){
			cost-=5;
			count_5+=1;
			continue;
		}
		if(cost>=1){
			cost-=1;
			count_1+=1;
			continue;
		}
	}
		cout <<  "50 dollar: " << count_50
			 << " 10 dollar: " << count_10
			 << "  5 dollar: " << count_5
			 << "  1 dollar: " << count_1;
}
