#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char text[2000], plain[2000];
    const char english[] = "ETAOINSHRDLCUMWFGYPBVKJXQZ";
    int freq[26] = {0}, order[26];

    printf("Ciphertext: ");
    fgets(text, sizeof(text), stdin);

    for (int i = 0; text[i]; i++)
        if (isalpha((unsigned char)text[i]))
            freq[toupper((unsigned char)text[i]) - 'A']++;

    for (int r = 0; r < 26; r++) {
        int best = -1, idx = -1;
        for (int j = 0; j < 26; j++)
            if (freq[j] > best) { best = freq[j]; idx = j; }
        order[r] = idx;
        freq[idx] = -1;
    }

    for (int guess = 0; guess < 10; guess++) {
        int map[26];
        for (int r = 0; r < 26; r++)
            map[order[r]] = english[(r + guess) % 26];

        for (int i = 0; text[i]; i++) {
            if (isalpha((unsigned char)text[i])) {
                char c = map[toupper((unsigned char)text[i]) - 'A'];
                plain[i] = islower((unsigned char)text[i]) ? tolower(c) : c;
            } else plain[i] = text[i];
        }
        printf("\nCandidate %d:\n%s", guess + 1, plain);
    }
    return 0;
}
