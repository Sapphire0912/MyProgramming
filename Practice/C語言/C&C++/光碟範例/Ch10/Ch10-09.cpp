#include "Ch10-09.h"    // 含括字串類別定義

int main()
{
  Str s1("Bjarne "), s2("Stroustrup");
  (s1 + s2 + " designed C++").show(); // 將物件與字串常數加在一起
}
