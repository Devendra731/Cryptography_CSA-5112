#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char s[300];
    int key[]={9,0,1,7,23,15,21,14,11,11,2,8,9};
    int nkey=13, k=0;
    printf("Message (letters only, max 13): ");
    scanf("%299s",s);

    for (int i=0;s[i];i++) {
        if (!isalpha((unsigned char)s[i])) continue;
        if (k>=nkey) { puts("\nKey stream too short."); return 1; }
        int x=toupper((unsigned char)s[i])-'A';
        putchar('A'+(x+key[k++])%26);
    }
    return 0;
}
