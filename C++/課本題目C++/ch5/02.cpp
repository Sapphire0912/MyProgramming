#include<iostream>
using namespace std;

main(){
	float score;
	cout << "Enter the score of student: ";
	cin >> score;
	if(90<=score<=100)
		cout << "The score is degree A." << endl;
	if(80<=score<90)
		cout << "The score is degree B." << endl;
	if(70<=score<80)
		cout << "The score is degree C." << endl;
	if(60<=score<70)
		cout << "The score is degree D." << endl;
	if(score<60)
		cout << "The score is degree E. Flank!!!" << endl;
}
