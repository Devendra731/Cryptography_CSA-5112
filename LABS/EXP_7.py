#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char c[1000], order[] = "ETAOINSHRDLCUMWFGYPBVKJXQZ";
    int count[26] = {0}, rank[26], n = 0;

    printf("Ciphertext: ");
    fgets(c, sizeof(c), stdin);

    for (int i = 0; c[i]; i++)
        if (isalpha((unsigned char)c[i])) count[toupper(c[i]) - 'A']++;

    for (int r = 0; r < 26; r++) {
        int best = -1, idx = -1;
        for (int j = 0; j < 26; j++)
            if (count[j] > best) { best = count[j]; idx = j; }
        if (idx >= 0) { rank[idx] = r; count[idx] = -1; }
    }

    for (int i = 0; c[i]; i++) {
        if (isalpha((unsigned char)c[i])) {
            int x = toupper(c[i]) - 'A';
            char q = order[rank[x]];
            putchar(islower((unsigned char)c[i]) ? tolower(q) : q);
        } else putchar(c[i]);
    }
    return 0;
}
