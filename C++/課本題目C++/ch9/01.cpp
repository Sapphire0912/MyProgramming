#include<iostream>
using namespace std;

class Car{
	public:
		Car(double,double);
		void show(){
			cout << "Gas: " << gas
				 << " Weight: " << weight << endl;
		};
	private:
		double gas;
		double weight;
};

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
}

main(){
	Car c(50,8000);
	c.show();
}
