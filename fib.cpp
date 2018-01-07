
using namespace std;
long long fib(int x)
{
  long long first = 0;
  long long second = 1;
  long long b;
  int a = 1;
  if (x <=1)
    return x;
  else
  {
  for ( a = 1; a < x; a++)
  {
    b = first + second;
    first = second;
    second = b;
  }
  return b;
}
}
