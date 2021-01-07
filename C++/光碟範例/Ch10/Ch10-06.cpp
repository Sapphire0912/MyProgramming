#include "Ch10-06.h"    // 含括字串類別定義

int main()
{
  Str s1("moon "), s2("cake");
  s1[0] = 'n';   // 修改字串中第 1 個字元
  s2[2] = 'f';   // 修改字串中第 3 個字元
  (s1+s2).show();
}
