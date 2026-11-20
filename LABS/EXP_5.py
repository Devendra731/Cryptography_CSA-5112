#include <stdio.h>
#include <ctype.h>

int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}

int main(void) {
    char text[500];
    int a, b;

    printf("Text: ");
    fgets(text, sizeof(text), stdin);
    printf("Enter a and b (gcd(a,26) must be 1): ");
    scanf("%d%d", &a, &b);

    a = (a % 26 + 26) % 26;
    b = (b % 26 + 26) % 26;
    if (gcd(a, 26) != 1) {
        puts("Invalid a: it must be coprime with 26.");
        return 1;
    }

    for (int i = 0; text[i]; i++) {
        if (isalpha((unsigned char)text[i])) {
            int base = isupper((unsigned char)text[i]) ? 'A' : 'a';
            int x = text[i] - base;
            text[i] = (char)(base + (a * x + b) % 26);
        }
    }
    printf("Ciphertext: %s", text);
    return 0;
}
