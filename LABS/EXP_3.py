#include <stdio.h>
#include <ctype.h>
#include <string.h>

char sq[5][5];

void make_square(const char *key) {
    int used[26] = {0}, n = 0;
    char s[26];
    used['J' - 'A'] = 1;

    for (int pass = 0; pass < 2; pass++) {
        const char *p = pass ? "ABCDEFGHIKLMNOPQRSTUVWXYZ" : key;
        for (; *p; p++) {
            char c = toupper((unsigned char)*p);
            if (c == 'J') c = 'I';
            if (c >= 'A' && c <= 'Z' && !used[c - 'A']) {
                used[c - 'A'] = 1;
                s[n++] = c;
            }
        }
    }
    for (int i = 0; i < 25; i++) sq[i / 5][i % 5] = s[i];
}

void pos(char c, int *r, int *col) {
    if (c == 'J') c = 'I';
    for (*r = 0; *r < 5; (*r)++)
        for (*col = 0; *col < 5; (*col)++)
            if (sq[*r][*col] == c) return;
}

int main(void) {
    char key[100], text[500], p[500];
    printf("Keyword: "); scanf("%99s", key);
    make_square(key);
    printf("Plaintext: "); scanf(" %499[^\n]", text);

    int n = 0;
    for (int i = 0; text[i]; i++)
        if (isalpha((unsigned char)text[i])) {
            char c = toupper((unsigned char)text[i]);
            p[n++] = (c == 'J') ? 'I' : c;
        }
    p[n] = '\0';

    char out[1000];
    int k = 0;
    for (int i = 0; i < n;) {
        char a = p[i++], b;
        if (i == n) b = 'X';
        else if (p[i] == a) b = 'X';
        else b = p[i++];

        int r1,c1,r2,c2;
        pos(a,&r1,&c1); pos(b,&r2,&c2);
        if (r1 == r2) {
            out[k++] = sq[r1][(c1+1)%5];
            out[k++] = sq[r2][(c2+1)%5];
        } else if (c1 == c2) {
            out[k++] = sq[(r1+1)%5][c1];
            out[k++] = sq[(r2+1)%5][c2];
        } else {
            out[k++] = sq[r1][c2];
            out[k++] = sq[r2][c1];
        }
    }
    out[k] = '\0';
    printf("Ciphertext: %s\n", out);
    return 0;
}
