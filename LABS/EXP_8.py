#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char key[100], text[500], map[26];
    int used[26] = {0}, n = 0;

    printf("Keyword: ");
    scanf("%99s", key);
    for (int i = 0; key[i]; i++) {
        int x = toupper((unsigned char)key[i]) - 'A';
        if (x >= 0 && x < 26 && !used[x]) {
            used[x] = 1; map[n++] = 'A' + x;
        }
    }
    for (int i = 0; i < 26; i++)
        if (!used[i]) map[n++] = 'A' + i;

    getchar();
    printf("Plaintext: ");
    fgets(text, sizeof(text), stdin);

    for (int i = 0; text[i]; i++) {
        if (isalpha((unsigned char)text[i])) {
            int x = toupper((unsigned char)text[i]) - 'A';
            char q = map[x];
            putchar(islower((unsigned char)text[i]) ? tolower(q) : q);
        } else putchar(text[i]);
    }
    return 0;
}
