#include <stdio.h>
#include <cstdlib>

void update(int *a,int *b) {
    // Complete this function 
    int w = *a;
    *a = *a+*b;
    *b=abs(w-*b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
