#include <stdio.h>
#include <ctype.h>

int main(void) {
    char text[500];
    int shift;

    printf("Text: ");
    fgets(text, sizeof(text), stdin);
    printf("Shift (1-25): ");
    scanf("%d", &shift);
    shift = ((shift % 26) + 26) % 26;

    for (int i = 0; text[i]; i++) {
        if (isalpha((unsigned char)text[i])) {
            char base = isupper((unsigned char)text[i]) ? 'A' : 'a';
            text[i] = (char)(base + (text[i] - base + shift) % 26);
        }
    }
    printf("Ciphertext: %s", text);
    return 0;
}
