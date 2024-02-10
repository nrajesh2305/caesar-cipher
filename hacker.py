
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

message = "Meet me by the rose bushes tonight."
print(encrypt_message(message, 4))

def decrypt_message(message, key):
    pass