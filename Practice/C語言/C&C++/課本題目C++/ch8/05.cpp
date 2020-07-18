#include<iostream>
using namespace std;

class Student{
	public:
		void set(char*,char*);
		double score(int,int,int);
		double avg();
		void show();
	private:
		char* Name;
		char* ID;
		double eng,math,cplus;
};

void Student::set(char* name,char* id){
	this->Name=name;
	this->ID=id;
}

void Student::show(){
	cout << "Name: " << Name << "  ID: " << ID << endl;
}

double Student::score(int EN,int Math,int C){
	eng=EN;
	math=Math;
	cplus=C;
}

double Student::avg(){
	cout << "Average: " << (eng+math+cplus)/3 << endl;
}


int main(){
	Student Data;
	Data.set("Sapphire","0912");
	Data.score(76,84,99);
	Data.show();
	Data.avg();
}
