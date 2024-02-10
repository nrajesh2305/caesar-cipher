
# Replace with portfolio website when done.
website_url = ""

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def printIntro():
    print("Caesar Cipher, by Nithin Rajesh " + website_url + "\n")

# Works 100%
def encrypt_message(message, key):
    encrypted_message = ""
    for letter in message:
        letter = letter.upper()
        if(letter not in alphabet):
            encrypted_message += letter
            continue
        if(alphabet.index(letter) + key > len(alphabet)):
            letter = alphabet[(alphabet.index(letter) + key) - len(alphabet)]
        else:
            letter = alphabet[alphabet.index(letter) + key]
        encrypted_message += letter
    return encrypted_message

# Works 100%
def decrypt_message(message, key):
    decrypted_message = ""
    for letter in message:
        letter = letter.upper()
        if(letter not in alphabet):
            decrypted_message += letter
            continue
        if(alphabet.index(letter) - key < 0):
            letter = alphabet[len(alphabet) - alphabet.index(letter)]
        else:
            letter = alphabet[alphabet.index(letter) - key]
        decrypted_message += letter
    return decrypted_message