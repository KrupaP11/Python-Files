text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'
#this is to define a function
def vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        
        #Append any non-letter character to the message
        if not char.isalpha():
#is.alpha() methond return true if all character of string on which it is called are letter.
            final_message += char
        else:

            #Find the right key character to encode/decode
            key_char = key[key_index % len(key)] # % is remainder
            key_index += 1

            #Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            # .index() is similar to .find()
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            #len() is a length function
            final_message += alphabet[new_index]
            #anything within pranthesis is called an argument

    return final_message

def encrypt(message, key):
    return vigenere(message, key)
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
