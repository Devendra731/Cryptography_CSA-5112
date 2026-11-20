#include <stdio.h>

int mod(int x) { x%=26; return x<0?x+26:x; }
int inv(int x) {
    for (int i=1;i<26;i++) if (mod(x*i)==1) return i;
    return -1;
}
int main(void) {
    /* Plaintext columns: (2,4), (1,3); ciphertext: (0,10), (2,17) */
    int a=2,b=1,c=4,d=3, det=mod(a*d-b*c), di=inv(det);
    if (di<0) { puts("Plaintext matrix is not invertible."); return 1; }

    int P[2][2]={{a,b},{c,d}}, C[2][2]={{0,2},{10,17}}, I[2][2];
    I[0][0]=mod(d*di); I[0][1]=mod(-b*di);
    I[1][0]=mod(-c*di); I[1][1]=mod(a*di);

    puts("Recovered key matrix:");
    for (int i=0;i<2;i++) {
        for (int j=0;j<2;j++) {
            int v=0;
            for (int k=0;k<2;k++) v+=C[i][k]*I[k][j];
            printf("%d ",mod(v));
        }
        puts("");
    }
    return 0;
}
