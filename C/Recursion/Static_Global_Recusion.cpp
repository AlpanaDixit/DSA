#include <stdio.h>

int x =0;
int fun(int n)
{

    // int x =0;
    // static int x=0;
    if (n>0)
    {
        x++;
        return fun(n-1)+x;

    }
}
int main(){
    int r;
    r = fun(5);
    printf("%d ",r);
    return 0;
}