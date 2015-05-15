message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

phrase = 'The secret password is Rosebud.'
phrase = 'BPM AMKZMB XIAAEWZL QA ZWAMJCL.'
phrase = 'The password is 31337.'
phrase = 'GUVF VF ZL FRPERG ZRFFNTR.'
#key = 30

phrase = phrase.upper()
length = len(LETTERS)

#for letter in phrase:
#    if letter in LETTERS:
#        index = (LETTERS.index(letter) + key) % length
#        enphrase += LETTERS[index]
#    else:
#        enphrase += letter

for key in range(length):
    enphrase = str()
    for letter in phrase:
        if letter in LETTERS:
            index = (LETTERS.index(letter) + key) % length
            enchar = LETTERS[index]
        else:
            enchar = letter
        enphrase += enchar
    print('Key #%d: %s' % (key, enphrase))
