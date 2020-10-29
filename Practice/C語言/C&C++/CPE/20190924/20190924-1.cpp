#include<iostream>
#include<cmath>
using namespace std;

main(){
	int test,x,a,b;
	cin >> test;
	int ans[test];
	for(x=0;x<test;x++){
		char ch1,ch2;
		long long m=0,i,j,sym=0;
		cin >> ch1 >> ch2 >> m;
			long long matrix[m][m];
			for(i=0;i<m;i++){
				for(j=0;j<m;j++){
					cin >> matrix[i][j];
				}
			}
		for(i=0;i<m;i++){
			for(j=0;j<m;j++){
				a=abs(m-i-1);
				b=abs(m-j-1);
				if(matrix[i][j]!=matrix[a][b] || matrix[i][j]<0){
					sym=0;
					break;	
				}
				else{
					sym=1;
				}	
			}
			ans[x]=sym;
		}
	}
	for(x=0;x<test;x++){
		if(ans[x]==0){
			cout << "Test #" << x+1 << ":" << " Non-symmetric."
				 << endl;
		}
		else{
			cout << "Test #" << x+1 << ":" << " Symmetric."
				 << endl;
		}
	}
}
