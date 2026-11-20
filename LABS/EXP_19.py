#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>

int main(void) {
    unsigned char key[24] = "12345678901234567890123";
    unsigned char iv[8]  = "12345678";
    unsigned char plain[] = "Cryptography lab";
    unsigned char cipher[128], recovered[128];
    int n, total;

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    EVP_EncryptInit_ex(ctx, EVP_des_ede3_cbc(), NULL, key, iv);
    EVP_EncryptUpdate(ctx, cipher, &n, plain, (int)strlen((char*)plain));
    total = n;
    EVP_EncryptFinal_ex(ctx, cipher + total, &n);
    total += n;

    printf("Ciphertext: ");
    for (int i=0; i<total; i++) printf("%02X", cipher[i]);
    putchar('\n');

    EVP_DecryptInit_ex(ctx, EVP_des_ede3_cbc(), NULL, key, iv);
    EVP_DecryptUpdate(ctx, recovered, &n, cipher, total);
    int outlen = n;
    EVP_DecryptFinal_ex(ctx, recovered + outlen, &n);
    outlen += n;
    recovered[outlen] = '\0';

    printf("Decrypted: %s\n", recovered);
    EVP_CIPHER_CTX_free(ctx);
    return 0;
}
