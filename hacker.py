
# Replace with portfolio website when done.
website_url = ""

print("Caesar Cipher, by Nithin Rajesh " + website_url + "\n")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Works 100%
def encrypt_message(message, key):
    encrypted_message = ""
    for letter in message:
        if(letter.upper() not in alphabet):
            encrypted_message += letter.upper()
            continue
        if(alphabet.index(letter.upper()) + key > len(alphabet)):
            letter = alphabet[(alphabet.index(letter.upper()) + key) - len(alphabet)]
        else:
            letter = alphabet[alphabet.index(letter.upper()) + key]
        encrypted_message += letter.upper()
    return encrypted_message

# Works 100%
def decrypt_message(message, key):
    decrypted_message = ""
    for letter in message:
        if(letter.upper() not in alphabet):
            decrypted_message += letter.upper()
            continue
        if(alphabet.index(letter.upper()) - key < 0):
            letter = alphabet[len(alphabet) - key]
        else:
            letter = alphabet[alphabet.index(letter.upper()) - key]
        decrypted_message += letter.upper()
    return decrypted_message