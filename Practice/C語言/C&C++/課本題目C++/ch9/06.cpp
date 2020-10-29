#include<iostream>
using namespace std;

struct Point{
	double x;
	double y;
};

class Rectangle{
	public:
		Rectangle(Point,double,double); // (x1,y1) (length*width)
		Rectangle(Point,Point); // (x1,y1) (x2,y2)
	private:
		double length;
		double width;
};
