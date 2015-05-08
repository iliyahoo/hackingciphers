spam = 42

def eggs():
    spam = 99 # spam in this function is local
    print('In eggs():', spam)

def ham():
    print('In ham():', spam) # spam in this function is global

def bacon():
    global spam # spam in this function is global
    print('In bacon():', spam)
    spam = 0

def CRASH():
    print(spam) # spam in this function is local
    spam = 0

#print(spam)
#eggs()
#print(spam)
#ham()
#print(spam)
#bacon()
#print(spam)
#CRASH()

text = 'Common sense is not so common.'
text = 'RDBBDC HTCHT XH CDI HD RDBBDC.'
key = 15

LENGTH = len(text)
A = ord('A')
Z = ord('Z')

ABC = ''
for i in range(A, Z + 1):
    ABC += chr(i)

text = text.upper()
for count in range(1, LENGTH):
    encrypted = ''
    for letter in text:
        if letter in ABC:
            encrypted += chr(((ord(letter) - A - count) % 26) + A)
        else:
            encrypted += letter
    print(count, encrypted)
