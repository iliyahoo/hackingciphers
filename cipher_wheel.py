#!/usr/bin/python3

phrase = 'bpm amkzmb xiaaewzl qa zwamjcl.'
phrase = 'The secret password is Rosebud.'
key = 8
#phrase = 'Iwt ctl ephhldgs xh Hldgsuxhw.'
#key = 15

def cypher_wheel(action, phrase, key):
    if action == 'decrypt':
        key *= -1
    phrase = phrase.lower()
    char_a = ord('a')
    char_z = ord('z')
    
    enphrase = str()
    
    for char in phrase:
        converted = ord(char)
        if converted not in range(char_a, char_z + 1):
            enchar = char
        else:
            char = chr((ord(char) - char_a + key) % (len(range(char_a, char_z)) + 1) + char_a)
        enphrase += char
    return(enphrase)

result = cypher_wheel('encrypt', phrase, key)
print(result)
