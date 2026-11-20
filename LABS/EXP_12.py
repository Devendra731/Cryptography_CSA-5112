#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char s[500], p[500];
    int K[2][2]={{9,4},{5,7}}, inv[2][2]={{5,24},{15,25}};
    printf("Text (letters only): ");
    scanf("%499s",s);

    int n=(int)strlen(s);
    if (n%2) { s[n++]='X'; s[n]='\0'; }

    printf("Cipher: ");
    for (int i=0;i<n;i+=2) {
        int x=toupper(s[i])-'A', y=toupper(s[i+1])-'A';
        printf("%c%c",'A'+(K[0][0]*x+K[0][1]*y)%26,
                      'A'+(K[1][0]*x+K[1][1]*y)%26);
    }
    printf("\nDecrypted: ");
    for (int i=0;i<n;i+=2) {
        int x=toupper(s[i])-'A', y=toupper(s[i+1])-'A';
        p[i]='A'+(inv[0][0]*x+inv[0][1]*y)%26;
        p[i+1]='A'+(inv[1][0]*x+inv[1][1]*y)%26;
    }
    p[n]='\0';
    puts(p);
    return 0;
}
