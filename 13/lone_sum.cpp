#include <iostream>

int lonesum(int a, int b , int c) {
  if (a == b == c)
    std::cout << 0 << '\n';
  if (a == b)
    std::cout << c << '\n';
  if (c == b )
    std::cout << a << '\n';
  if ( c == a )
    std::cout << b << '\n';

  return 0;
}


bool cigar_party(int cigars, bool is_weekend){
  if(cigars < 40){
    return false;
  }
  else if(cigars > 60 && !is_weekend){
    return false;
  }
  else{
    return true;
  }
