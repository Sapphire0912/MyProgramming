#include "Ch10-08.h"    // 含括字串類別定義

int main()
{
  char s1[] = "Mickey ";
  Str s2 ="Mighty", s3 ="Magic ";
  s2 = s1;            // 將字元陣列指定給物件
  s2.show();
  s3 = s2 = "Mouse";  // 將常數字串指定給物件
  s3.show();
}
