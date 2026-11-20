#include <stdio.h>
#include <ctype.h>
#include <string.h>

char sq[5][5];

void build(char *key) {
    int seen[26] = {0}, n = 0;
    char all[200];
    strcpy(all, key);
    strcat(all, "ABCDEFGHIKLMNOPQRSTUVWXYZ");
    seen['J'-'A'] = 1;
    for (int i = 0; all[i]; i++) {
        char c = toupper((unsigned char)all[i]);
        if (c == 'J') c = 'I';
        if (c >= 'A' && c <= 'Z' && !seen[c-'A']) {
            seen[c-'A'] = 1;
            sq[n/5][n%5] = c;
            n++;
        }
    }
}
void pos(char c, int *r, int *k) {
    if (c == 'J') c = 'I';
    for (*r=0; *r<5; (*r)++)
        for (*k=0; *k<5; (*k)++)
            if (sq[*r][*k] == c) return;
}
int main(void) {
    char key[]="MONARCHY", c[500];
    build(key);
    printf("Ciphertext (even number of letters): ");
    scanf("%499s", c);

    for (int i=0; c[i] && c[i+1]; i+=2) {
        int r1,k1,r2,k2;
        pos(toupper(c[i]),&r1,&k1); pos(toupper(c[i+1]),&r2,&k2);
        if (r1==r2) printf("%c%c",sq[r1][(k1+4)%5],sq[r2][(k2+4)%5]);
        else if (k1==k2) printf("%c%c",sq[(r1+4)%5][k1],sq[(r2+4)%5][k2]);
        else printf("%c%c",sq[r1][k2],sq[r2][k1]);
    }
    return 0;
}
