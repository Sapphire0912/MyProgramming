#include<iostream>
using namespace std;

class Dates{
	public:
		Dates();
		char* askDate(int); 
	private:
		char* week[7];
};

Dates::Dates(){
	week[0]="Mon";
	week[1]="Tue";
	week[2]="Wed";
	week[3]="Thu";
	week[4]="Fri";
	week[5]="Sat";
	week[6]="Sun";
}

char* Dates::askDate(int pos){
	if(pos>7){
		cout << "Warning: The number is bigger than length of array. (Default: pos = 7)" << endl;
		pos = 7;
	}
	else if(pos<1){
		cout << "Warning: The number is lower than length of array. (Default: pos = 1)" << endl;
		pos = 1;
	}
	return week[pos-1];
}

main(){
	Dates w;
	int i;
//	cout << "Enter one num: " ;
//	cin >> i;
//	cout << w.askDate(i);
	cout << "Week: ";
	for(i=1;i<=7;i++){
		cout << w.askDate(i) << " ";
	}
}

