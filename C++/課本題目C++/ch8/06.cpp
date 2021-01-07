#include<iostream>
using namespace std;

class Student{
	public:
		void set(char*,char*);
		double score(double,double,double);
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

double Student::score(double EN,double Math,double C){
	eng=EN;
	math=Math;
	cplus=C;
}

double Student::avg(){
	return (eng+math+cplus)/3;
}


int main(){
	Student *Data[5];
	for(int i=0;i<5;i++){
		Data[i]=new Student();
	}
	Data[0]->set("Sapphire","0912");
	Data[1]->set("Eric","1002");
	Data[2]->set("Iris","1224");
	Data[3]->set("Aurora","0629");
	Data[4]->set("Lily","0930");
	
	Data[0]->score(70,80,90);
	Data[1]->score(83.5,79,69.6);
	Data[2]->score(92.5,90,100);
	Data[3]->score(100,75,88.4);
	Data[4]->score(60,72.5,90.1);
	
	Student* temp;
	for(int i=0;i<5;i++){
		for(int j=i+1;j<5;j++){
			if(Data[i]->avg()>Data[i]->avg()){
				temp=Data[i];
				Data[i]=Data[j];
				Data[j]=temp;
			}
		}
	}
	for(int i=0;i<5;i++){
		Data[i]->show();
		cout << "Average: " << Data[i]->avg() << endl << endl;
	}
}
