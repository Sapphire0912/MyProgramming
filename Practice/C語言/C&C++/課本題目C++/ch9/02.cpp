#include<iostream>
using namespace std;

class Car{
	public:
		Car(double,double);
		~Car();
		int howmany(){return counter;}
		void show(){
			cout << "Gas: " << gas
				 << " Weight: " << weight << endl;
		};
	private:
		double gas;
		double weight;
		static int counter;
};

int Car::counter = 0;

Car::Car(double Max_gas, double Limit_weight){
	if(Max_gas > 60){
		Max_gas = 60;
		cout << "Error."<< endl;
		cout << "Out of range." << endl;
	}
	gas = Max_gas;
	
	if(Limit_weight > 5000){
		Limit_weight = 5000;
		cout << "Error."<< endl;
		cout << "Out of range." << endl;
	}
	weight = Limit_weight;
	counter++;
}

Car::~Car(){
	counter--; 
}

main(){
	Car t(30,2000);
	cout << "現在有 " << t.howmany() << "輛車\n";
	
	Car *mid = new Car(40,1300);
	Car *muv = new Car(55,4000);
	cout << "現在有 " << t.howmany() << "輛車\n";
	
	delete mid;
	delete muv;
	cout << "現在有 " << t.howmany() << "輛車\n";
}
