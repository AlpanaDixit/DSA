#include <iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

struct Rectangle
{
    int length;
    int bredth;

};

int main()
{
    struct Rectangle r={10,5};
    cout<<r.length<<endl;
    cout<<r.bredth<<endl;

    Rectangle *p=&r;
    cout<<p->length<<endl;
    cout<<p->bredth<<endl;

    return 0;
};