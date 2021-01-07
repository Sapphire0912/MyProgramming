#include "Ch10-02.h"

int main()
{
  Str test("Bjarne Stroustrup ");
  // 因 . 運算子較優先, 所以要加上括號
  (+test).show();    // 全部大寫
  test.show();
  (-test).show();    // 全部小寫
}
