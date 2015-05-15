#!/usr/bin/python3


from transpositionEncrypt import encrypt, decrypt
import sys, time, os.path as path



def main():
    inFile = 'frankenstein.txt'
    outFile = 'frankenstein.encrypted.txt'
    mode = 'encrypt'

    inFile = 'frankenstein.encrypted.txt'
    outFile = 'frankenstein.decrypted.txt'
    mode = 'decrypt'

    key = 10

    if not path.exists(inFile):
        print('The %s file does not exust.' % inFile)
        sys.exit()

    if path.exists(outFile):
        response = input(
'''This will overwrite the file %s.
(C)ontinue or (Q)uite?    ''' % outFile)
        if not response.upper().startswith('C'):
            sys.exit()

    print('%sing...' % mode.title())
    startTime = time.time()

    fd = open(inFile)
    text = fd.read()
    fd.close()

    if mode == 'encrypt':
        translated = encrypt(text, key)
    elif mode == 'decrypt':
        translated = decrypt(text, key)

    print('%sion time: %s seconds' % (mode.title(), round(time.time() - startTime, 2)))

    fd = open(outFile, 'w')
    fd.write(translated)
    fd.close()

    print('Done %sing %s (%s characters).' % (mode, inFile, len(translated)))
    print('%sed file is %s.' % (mode.title(), outFile))



if __name__ == "__main__":
    main()
