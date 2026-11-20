#include <stdio.h>
#include <stdint.h>

int main(void) {
    /* Toy blocks show CBC error propagation rules, not real encryption. */
    uint8_t P[4]  = {0x10, 0x20, 0x30, 0x40};
    uint8_t C[4]  = {0xA1, 0xB2, 0xC3, 0xD4};
    uint8_t altered[4];

    puts("ECB: C1 corruption affects only decrypted P1.");
    for (int i=0; i<4; i++) {
        altered[i] = P[i];
        if (i == 1) altered[i] ^= 0x01;  /* corrupted block 1 */
        printf("P%d original=%02X received=%02X\n",
               i+1, P[i], altered[i]);
    }

    puts("\nCBC: corruption in C1 affects P1 and flips same bit in P2.");
    for (int i=0; i<4; i++) {
        uint8_t p = P[i];
        if (i == 1) p ^= 0x01;          /* P1 becomes unpredictable */
        if (i == 2) p ^= 0x01;          /* corresponding bit flips in P2 */
        printf("P%d original=%02X received=%02X\n", i+1, P[i], p);
    }

    puts("\nCBC: later blocks after P2 are unaffected by a C1 bit error.");
    (void)C;
    return 0;
}
