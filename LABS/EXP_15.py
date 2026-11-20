#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c[1000], p[1000];
    printf("Ciphertext: ");
    fgets(c,sizeof(c),stdin);

    for (int shift=0;shift<26;shift++) {
        for (int i=0;c[i];i++) {
            if (isalpha((unsigned char)c[i])) {
                int base=islower((unsigned char)c[i])?'a':'A';
                p[i]=(char)(base+(c[i]-base-shift+26)%26);
            } else p[i]=c[i];
        }
        printf("Shift %2d: %s",shift,p);
    }
    return 0;
}
