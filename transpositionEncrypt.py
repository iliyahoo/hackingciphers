#!/usr/bin/python


action = 'decrypt'
key = 8



def main():
    if action == 'encrypt':
        text = 'Common sense is not so common.'
        print(encrypt(text, key))
    elif action == 'decrypt':
        text = 'Cenoonommstmme oo snnio. s s c'
        print(decrypt(text, key))
    else:
        exit()



def encrypt(text, key):
    length = len(text)
    encrypted = str()

    for index in range(key):
        for count in range(index, length, key):
            encrypted += text[count]

    return(encrypted)



def decrypt(text, key):
    # get number of columns
    if (len(text) % key) != 0:
        columns = len(text) // key + 1
    else:
        columns = len(text) // key

    # get empty cells indexes list
    unused = key * columns - len(text)
    matrix = list()
    for column in range(columns):
        for row in range(key):
            matrix.append(row * columns + column)
    empty = matrix[-unused:]

    # convert the string into list and insert "|" sign in place of empty cells
    text = list(text)
    for index in empty:
        text.insert(index, "|")

    # decrypt the message
    lst = list()
    for column in range(columns):
        for row in range(key):
            letter = text[row * columns + column]
            lst.append(letter)
    text = ''.join(lst).rstrip("|")

    return(text)



if __name__ == '__main__':
    main()



# >>> import transpositionEncrypt as crypt
# >>> crypt.encrypt(text,key)
# >>> crypt.decrypt(text,key)
