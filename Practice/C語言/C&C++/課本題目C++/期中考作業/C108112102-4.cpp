#include<iostream>
#define students 10
/* 
	½Ò¥»ch7-62 ²Ä10ÃD
*/
 
using namespace std;
float average(int[],int);
int sum(int[],int);

int main(){
	int score[3],total[10];
	float avg[10];
	for(int i=1;i<=students;i++){
		cout << "Enter students grades(CH,EN,MATH): " << endl;
		for(int s=0;s<sizeof(score)/4;s++){
			cin >> score[s];
		}
		avg[i-1]=average(score,sizeof(score)/4);
		total[i-1]=sum(score,sizeof(score)/4);
	}
	cout << "Average of " << students << " students : " << endl;
	for(int i=0;i<students;i++){
		cout << "NO " << i+1 << " : " << avg[i]
			 << endl;
	}
	cout << "Total score of " << students << " students : " << endl;
	for(int j=0;j<students;j++){
		cout << "NO " << j+1 << " : " << total[j]
			 << endl;
	}
}

float average(int score[],int len){
	float aver=0;
	for(int i=0;i<len;i++)
		aver+=score[i];
	aver/=len;
	return aver;
}

int sum(int score[],int len){
	int total=0;
	for(int j=0;j<len;j++)
		total+=score[j];
	return total;
}
