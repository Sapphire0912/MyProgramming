#include<iostream>
using namespace std;

main(){
	int use_time=4*60+57;
	int cost=0;
	while(use_time>=0){
		if(use_time<120){
			use_time-=30;
			cost+=30;
		}
		if(use_time<240 && use_time>=120){
			use_time-=30;
			cost+=40;
		}
		if(use_time>=240){
			use_time-=30;
			cost+=60;
		}
	}
	cout << "Total:NT$ " << cost ; 
	return 0;
}
