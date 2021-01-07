#include<iostream>
using namespace std;

class Vehicle {
public:
  void setPrice(double p) { price = p;} // 砞﹚基ΘㄧΑ
  Vehicle(double p = 0, double s = 0)
  {
    price = p;  speed = s;
  }
protected:
  double price; // 基
  double speed; // 硉
};

class ExerciseTool {
public:
  void setPrice(int p) { price = p;}    // 砞﹚基ΘㄧΑ
  ExerciseTool(int p = 0, double w = 100)
  {
    price = p;  weight = w;
  }
protected:
  int price;    // 基
  double weight;// 秖
};

class Bicycle: public Vehicle, public ExerciseTool { // 膥┯
public:
  Bicycle(double i,double j,double k, bool b): Vehicle(i,j)
  {                             // ㊣ Vehicle 篶ㄧΑ
     weight = k;
     discBreak = b;
  }
  double howMuch() { return Vehicle::price; } // 肚 Vehicle
private:                                      // Θ
  bool discBreak;      // 琌ㄏノ盒焚
};

int main()
{
  Bicycle bike(8000,15,12,true);
  cout << bike.howMuch() << endl;       // 陪ボ基

  bike.Vehicle::setPrice(2999);         // ㊣ぃ
  bike.ExerciseTool::setPrice(3999);    // setPrice()
  cout << bike.howMuch() << endl;       // 琩э挡狦
}
