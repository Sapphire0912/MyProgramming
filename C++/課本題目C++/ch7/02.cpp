#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

main(){
	char en[26];
	srand(time(NULL));
	for(int i=0;i<26;i++){
		en[i]=char(rand() % (122-97+1)+97);
		for(int j=0;j+1<=i;j++){
			if(en[i]==en[j])
				i--;
		}
	}
	char temp;
	for(int i=0;i<26;i++){
		cout << en[i];
	}
	cout << endl;
	for(int i=0;i<26;i++){
		for(int j=0;j<=i;j++){
			if(en[i]<en[j]){
				temp=en[i];
				en[i]=en[j];
				en[j]=temp;	
			}
		}
	}
	for(int i=0;i<26;i++)
		cout << en[i] ;
	cout << endl;
}
