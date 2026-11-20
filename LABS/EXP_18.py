#include <stdio.h>
#include <stdint.h>

int PC1[56] = {
  57,49,41,33,25,17,9,1,58,50,42,34,26,18,
  10,2,59,51,43,35,27,19,11,3,60,52,44,36,
  63,55,47,39,31,23,15,7,62,54,46,38,30,22,
  14,6,61,53,45,37,29,21,13,5,28,20,12,4
};
int PC2[48] = {
  14,17,11,24,1,5,3,28,15,6,21,10,23,19,
  12,4,26,8,16,7,27,20,13,2,41,52,31,37,
  47,55,30,40,51,45,33,48,44,49,39,56,34,
  53,46,42,50,36,29,32
};
int shifts[16] = {1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1};

int main(void) {
    uint64_t key = 0x133457799BBCDFF1ULL;
    uint64_t perm = 0;
    for (int i=0; i<56; i++)
        perm = (perm << 1) | ((key >> (64-PC1[i])) & 1ULL);

    uint32_t C = (uint32_t)(perm >> 28) & 0x0FFFFFFF;
    uint32_t D = (uint32_t)perm & 0x0FFFFFFF;

    for (int round=0; round<16; round++) {
        int s=shifts[round];
        C=((C<<s)|(C>>(28-s))) & 0x0FFFFFFF;
        D=((D<<s)|(D>>(28-s))) & 0x0FFFFFFF;

        uint64_t joined=((uint64_t)C<<28)|D, subkey=0;
        for (int i=0; i<48; i++)
            subkey=(subkey<<1)|((joined>>(56-PC2[i]))&1ULL);

        printf("Round %2d: C=%07X D=%07X K=%012llX\n",
               round+1, C, D, (unsigned long long)subkey);
    }
    return 0;
}
