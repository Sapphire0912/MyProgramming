#include "Ch10-05.h"    // 含括字串類別定義

int main()
{
  Str s1("Bjarne "), s2("Stroustrup");
  (s1 + s2).show(); // 將兩個字串物件加在一起
  cout << endl;
  (s1 + s2 + " designed C++").show(); // 將物件與字串常數加在一起
}
