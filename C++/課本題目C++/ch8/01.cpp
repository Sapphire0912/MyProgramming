#include<iostream>
using namespace std;

class Triangle{
	public:
		int side_length(int,int,int);
	private:
		int first;
		int second;
		int third;
};

int Triangle::side_length(int a,int b,int c){
	if(a+b>=c && a+c>=b && b+c>=a){
		first=a;
		second=b;
		third=c;
		cout << "Suitable triangle side length."
			 << endl;
	}
	else{
		cout << "The length of both sides of the triangle is greater than the third side."
			 << endl;
	}
}

main(){
	Triangle length;
	length.side_length(1,2,5);
} 
