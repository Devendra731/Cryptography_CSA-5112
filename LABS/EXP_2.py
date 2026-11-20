#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char text[500], key[27];
    const char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    printf("Enter 26-letter substitution key: ");
    scanf("%26s", key);
    if (strlen(key) != 26) {
        puts("Key must contain 26 letters.");
        return 1;
    }

    printf("Text: ");
    getchar();
    fgets(text, sizeof(text), stdin);

    for (int i = 0; text[i]; i++) {
        if (isalpha((unsigned char)text[i])) {
            int upper = isupper((unsigned char)text[i]);
            int index = toupper((unsigned char)text[i]) - 'A';
            char mapped = key[index];
            text[i] = upper ? toupper((unsigned char)mapped)
                            : tolower((unsigned char)mapped);
        }
    }
    printf("Ciphertext: %s", text);
    return 0;
}
