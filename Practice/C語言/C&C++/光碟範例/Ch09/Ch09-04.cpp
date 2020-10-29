#include<iostream>
using namespace std;

class Car {
public:
  Car() { gas = 10; counter++; } // 盢猳秖砞 10, 璸计竟 1
  static const int howmany() { return counter; } // 肚璸计竟
private:
  double gas;            // 猳秖
  static double eff;     // 繰篈Θ
  static int counter;    // ン璸计竟
};

double Car::eff = 30.0;  // 縐猳瞯–そど 30 そń
int Car::counter = 0;    // 秨﹍ン计秖琌 0 

int main()
{
  Car goodcar[10];
  cout << "磅︽ Car goodcar[10]; , "
       << "瞷Τ " << Car::howmany() << " 进ó" << endl;

  Car *badcar = new Car;
  cout << "磅︽ Car *badcar = new Car; , "
       << "瞷Τ " << Car::howmany() << " 进ó" << endl;
}
