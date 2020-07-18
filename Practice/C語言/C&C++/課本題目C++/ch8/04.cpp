#include<iostream>
using namespace std;

class Student{
	public:
		void set(char*,char*);
		void show();
	private:
		char* Name;
		char* ID;
};

void Student::set(char* name,char* id){
	this->Name=name;
	this->ID=id;
}

void Student::show(){
	cout << "Name: " << Name << "  ID: " << ID << endl;
}

int main(){
	Student Data;
	Data.set("Sapphire","0912");
	Data.show();
}
