#include "Ch09-09.h"         // 含括自訂的含括檔

int main()
{
  Str a=5;  // 相當於 a="     ";
  a.show(); cout << endl;
  Str b("abcde");
  b.show(); cout << endl;
  Str c = Str("C++");
  c.show(); cout << endl;
  Str *d = new Str("阿善師");
  d->show();
  delete d;
}
