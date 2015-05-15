#!/usr/bin/python

from transpositionEncrypt import decrypt, encrypt
import sys, random


def main():
    random.seed(42)

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #%s:  "%s..."' % (i + 1, message[:50]))

        for key in range(1, len(message) + 1):
            encrypted = encrypt(message, key)
            decrypted = decrypt(encrypted, key)

            if message != decrypted:
                print('\nMismatch with key %s and message\n%s.' % (key, message))
                print('\n' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')



if __name__ == "__main__":
    main()
