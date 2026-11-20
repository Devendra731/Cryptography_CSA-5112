#include <stdio.h>
#include <ctype.h>

char sq[5][5] = {
    {'M','F','H','I','K'}, {'U','N','O','P','Q'},
    {'Z','V','W','X','Y'}, {'E','L','A','R','G'},
    {'D','S','T','B','C'}
};

void pos(char c, int *r, int *k) {
    if (c == 'J') c = 'I';
    for (*r=0; *r<5; (*r)++)
        for (*k=0; *k<5; (*k)++)
            if (sq[*r][*k] == c) return;
}
int main(void) {
    char s[500], p[500]; int n=0;
    printf("Plaintext: ");
    fgets(s,sizeof(s),stdin);

    for (int i=0;s[i];i++) if (isalpha((unsigned char)s[i])) {
        char c=toupper((unsigned char)s[i]);
        p[n++]=(c=='J')?'I':c;
    }
    for (int i=0;i<n;) {
        char a=p[i++], b;
        if (i==n) b='X';
        else if (p[i]==a) b='X';
        else b=p[i++];
        int r1,k1,r2,k2;
        pos(a,&r1,&k1); pos(b,&r2,&k2);
        if (r1==r2) printf("%c%c",sq[r1][(k1+1)%5],sq[r2][(k2+1)%5]);
        else if (k1==k2) printf("%c%c",sq[(r1+1)%5][k1],sq[(r2+1)%5][k2]);
        else printf("%c%c",sq[r1][k2],sq[r2][k1]);
    }
    return 0;
}
