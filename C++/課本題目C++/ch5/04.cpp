#include<iostream>
using namespace std;

main(){
	int use_time,cost=0;
	
	cout << "Enter the time(min): ";
	cin >> use_time;
	if(use_time<800)
		cost = use_time*0.9;
	if(800<=use_time<1500)		
		cost = use_time*0.9*0.9;
	if(use_time>1500)
	    cost = use_time*0.9*0.8;
	
	cout << "Cost:NT " << cost;
}
