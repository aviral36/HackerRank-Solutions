#include <stdlib.h>
#include<stdio.h>
#include<math.h>

int main() {
  
    int a;
    long int b;
    char c;
    float d;
    double e;
    scanf("%d %li %c %f %lf", &a,&b,&c,&d,&e);
    printf("%d\n",a);
    printf("%li\n",b);
    printf("%c\n", c);
    printf("%.3f\n", d);
    printf("%.9lf\n",e);
    return 0;
}
