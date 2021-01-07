#include <iostream>
using namespace std;
#include "Ch16-09.h"

int main()
{
  char* all[] = { // 代刚戈
    "zebra",
    "dog",
    "cat",
    "frog",
  };
  
  // ㄏノ獶妓把计
  int minOfAll = min<char*>(all,4); 
    
  cout << "all[] い程じ琌 all[" << minOfAll << 
    "]" << endl;
}