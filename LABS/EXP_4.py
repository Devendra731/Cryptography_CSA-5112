#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char text[500], key[100];
    printf("Plaintext: ");
    fgets(text, sizeof(text), stdin);
    printf("Key: ");
    scanf("%99s", key);

    int k = 0, len = (int)strlen(key);
    for (int i = 0; text[i]; i++) {
        if (isalpha((unsigned char)text[i])) {
            int base = isupper((unsigned char)text[i]) ? 'A' : 'a';
            int shift = toupper((unsigned char)key[k++ % len]) - 'A';
            text[i] = (char)(base + (text[i] - base + shift) % 26);
        }
    }
    printf("Ciphertext: %s", text);
    return 0;
}
