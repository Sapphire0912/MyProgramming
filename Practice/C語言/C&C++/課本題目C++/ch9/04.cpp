#include<iostream>
#include<cstring>
using namespace std;

class Dates{
	public:
		Dates();
		char* toChinese(char*);
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

char* Dates::toChinese(char *st){
	static char name[][7] = {"星期一","星期二","星期三","星期四","星期五","星期六","星期日"};
	for(int i=0;i<7;i++){
		if(strcmp(st,week[i]) == 0){
			return name[i];	
		}
	}
}

main(){
	Dates cw;
	for(int i=0;i<7;i++){
		cout << cw.askDate(i+1) << " " << cw.toChinese(cw.askDate(i+1)) << endl;
	}
}

