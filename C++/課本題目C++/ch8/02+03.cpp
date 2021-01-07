#include<iostream>
using namespace std;

class Car {   
//	friend double addgas(Car&,double); // 03.cpp Answer
public:       
  void init(double,double);       
  double getEff()   { return eff;} 
  double checkGas() { return gas;} 
  double go(double);  
//  double addgas(double); // 02.cpp Answer
private:      
  double gas; 
  double eff; 
};

double Car::go(double kilo)
{
  if (gas >= (kilo/eff)) { 
    gas -= kilo/eff;       
    cout << "The fuel tank also has " << checkGas() << " liter gasoline." << endl;
    if (gas == 0)             
      cout << "No gasoline¡I";
  } 
  else {
    cout << "The amount of gasoline is not enough, the current gasoline is only enough to run "
         << (kilo = gas * eff) << " kilometers." << endl;
    gas = 0;
  }
  return kilo;
}

void Car::init(double G,double E)
{
  gas = G;  
  eff= E;   
}

//double Car::addgas(double add){  // 02.cpp Answer
//	gas+=add;
//}

//double addgas(Car &c,double add){ // 03.cpp Answer
//	c.gas+=add;
//}


int main()
{
  Car super;            
  super.init(20,30);   
  cout << "Fuel-efficient car runs " << super.getEff()
       << " kilometers." << endl;
  cout << "The fuel tank has " << super.checkGas() << " liter gasoline." << endl;

//  super.addgas(10); // 02.cpp Answer
//  addgas(super,8);  // 03.cpp Answer
  cout << "The fuel tank has " << super.checkGas() << " liter gasoline." << endl;
  
  while (super.checkGas() > 0) {
    double kilo;
    cout << "Will you drive for a few kilometers now? " << endl;
    cin >> kilo;
    super.go(kilo);    
  }
}

