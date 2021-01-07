#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

/* 
	使用亂數函式產生整數 1~20 之間的 6 個不同亂數, 
    放入一維陣列中, 將其列印出來, 
    並輸入一個整數再利用指標的方式 循序搜尋 所輸入的資料是否在陣列中 
*/ 

bool search(int *num,int input){
	for(int i=0;i<6;i++){
		if (*(num+i) == input)
			return true;
	}
	return false;
}

main(){
	srand(time(NULL));
	int c;
	int num[6];
	int *p = num;
	
	for(int i=0;i<6;i++){
		c = rand() % (20) + 1;
		num[i] = c;
		for(int j=0;j<i;j++){
			if(num[j] == num[i]){
				i--;
				break;
			}
		}
	}
	
	cout << "陣列裡面的數字: ";
	for(int i=0;i<6;i++)
		cout << *(p+i) << " " ;
	cout << endl;
	
	int n;
	cout << "請輸入一個數字(1~20): ";
	cin >> n;
	if(search(p,n))
		cout << "數字 " << n << " 存在於此陣列中" << endl; 
	else
		cout << "數字 " << n << " 不存在此陣列中" << endl; 
}
