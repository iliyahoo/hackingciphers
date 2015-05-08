LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'

phrase = 'The secret password is Rosebud.'
phrase = 'BPM AMKZMB XIAAEWZL QA ZWAMJCL.'
phrase = 'The password is 31337.'
key = 30

phrase = phrase.upper()
length = len(LETTERS)
print(length)
enphrase = str()

for letter in phrase:
    if letter in LETTERS:
        index = (LETTERS.index(letter) + key) % length
        enphrase += LETTERS[index]
#    else:
#        enphrase += letter
print(enphrase)