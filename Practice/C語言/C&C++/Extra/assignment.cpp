#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

main(){
	int light[8]={0,0,0,0,0,0,0,0};
	int position,sign;
	
	while(1){
		cout << "Iuput format: (position sign)" << endl;
		cin >> position >> sign;
		
		if(position>7 || position<0 || sign>1 || sign<0){
			cout << "Format Error." << endl;
			break;
		}
		
		int check,total=0;
		light[position]=sign;
		
		for(check=0;check<sizeof(light)/4;check++){
			if(light[check]!=0)
				total+=pow(2,check);
		}
		cout << "light: " ;
		for(int show=7;show>=0;show--){
			cout << light[show];
		}
		cout << endl;
		cout << "0x"  << hex << setw(2) << setfill('0')<< total << endl;
	}
}
