#include<iostream>
using namespace std; 

/* 
   1. 設電力公司的電費計算方式分成三類: 
  (1) 家庭用電: 100度以下,2.5元/度 101~300度,3.3元/度 301度以上,4.2元/度
  (2) 工業用電: 基本費為100度,150元 超過部分每度1.9元
  (3) 營業用電: 0~300度,6元/度 301度以上,6.8元/度
  
  Q. 輸入用電類別及使用度數後,計算其應繳納費用如何?
  PS. 以上三種用電類別必須以函式方式撰寫
*/

double family();
double industry();
double open();

main(){
	int type;
	double spend;
	while(1){
		cout << "輸入用電類別: ((1)家庭用電,(2)工業用電,(3)營業用電)) ";	
		cin >> type;
		if(type==1)
			spend=family();
		if(type==2)
			spend=industry();
		if(type==3)
			spend=open();
		if(type>3 || type<1){
			cout << "Error." << endl;
			break;
		}
		cout << "Cost: NT$ " << spend << endl << endl;
	}
}

double family(){
	double e,cost=0;
	cout << "輸入使用電量(單位: 度) : " ;
	cin >> e;
	if(e<=100)
		cost=e*2.5;
	if(e>100 && e<301)
		cost=e*3.3;
	if(e>300)
		cost=e*4.2;
	return cost;
}

double industry(){
	double e,cost=0;
	cout << "輸入使用電量(單位: 度) : " ;
	cin >> e;
	if(e<=100)
		cost=150;
	else
		cost=(e-100)*1.9+150;
	return cost;
}

double open(){
	double e,cost=0;
	cout << "輸入使用電量(單位: 度) : " ;
	cin >> e;
	if(e<=300)
		cost=e*6;
	else
		cost=e*6.8;
	return cost;
}
