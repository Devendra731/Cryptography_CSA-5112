#include <stdio.h>
#include <string.h>
#include <ctype.h>

int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}

int inverse(int a) {
    for (int x = 1; x < 26; x++)
        if ((a * x) % 26 == 1) return x;
    return -1;
}

int main(void) {
    char c[1000], p[1000];
    printf("Ciphertext: ");
    fgets(c, sizeof(c), stdin);

    for (int a = 1; a < 26; a++) if (gcd(a, 26) == 1) {
        int ai = inverse(a);
        for (int b = 0; b < 26; b++) {
            for (int i = 0; c[i]; i++) {
                if (isalpha((unsigned char)c[i])) {
                    int base = isupper((unsigned char)c[i]) ? 'A' : 'a';
                    int y = toupper((unsigned char)c[i]) - 'A';
                    p[i] = (char)(base + (ai * (y - b + 26) % 26));
                } else p[i] = c[i];
            }
            p[strlen(c)] = '\0';
            printf("a=%d b=%d: %s", a, b, p);
        }
    }
    return 0;
}
