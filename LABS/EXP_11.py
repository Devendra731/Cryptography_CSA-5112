#include <stdio.h>
#include <math.h>

int main(void) {
    double bits = 0;
    for (int i=1; i<=25; i++) bits += log2((double)i);
    printf("Approximate key space: 2^%.2f\n", bits);
    printf("Approximate number of keys: %.0e\n", exp2(bits));
    return 0;
}
