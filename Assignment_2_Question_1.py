# Group Name: [DAN/EXT 73]

# Group Members:
# Patrick Burzynski - [399755]

# Question 1
"""This program reads text from a file, encrypts it using a simple Caesar shift,
then decrypts it to verify the original message is correctly restored."""
# Feedback noted from assignment 1, less comments (comments only kept relevant).

#Input
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

# Encrypt
def encrypt(text):
    result = ""

    for char in text:
        # lowercase letters
        if 'a' <= char <= 'z':
            if char <= 'm':
                shift = shift1 * shift2
                result += '0' + chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                shift = shift1 + shift2
                result += '1' + chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        # uppercase letters
        elif 'A' <= char <= 'Z':
            if char <= 'M':
                shift = shift1
                result += '2' + chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                shift = shift2 ** 2
                result += '3' + chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # keep other characters unchanged
        else:
            result += char
    return result
#Decrypt 
def decrypt(text):
    result = ""
    i = 0
    while i < len(text):
        # Marker detected
        if text[i] in "0123":
            marker = text[i]
            char = text[i + 1]
            # lowercase a-m
            if marker == '0': 
                shift = shift1 * shift2
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            #lowercase n-z  
            elif marker == '1': 
                shift = shift1 + shift2
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # uppercase A-M
            elif marker == '2': 
                shift = shift1
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # uppercase N-Z   
            elif marker == '3':
                shift = shift2 ** 2
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            i += 2  # skip marker + letter
        else:
            result += text[i]
            i += 1
    return result
#Verify
def verify(original, decrypted):
    if original == decrypted:
        print("\nVerification successful")
    else:
        print("\nVerification failed")       
# file handling 
with open("raw_text.txt", "r") as file:
    original_text = file.read()
encrypted_text = encrypt(original_text)

with open("encrypted_text.txt", "w") as file:
    file.write(encrypted_text)
decrypted_text = decrypt(encrypted_text)

with open("decrypted_text.txt", "w") as file:
    file.write(decrypted_text)
#output 
print("\nEncrypted Text:\n")
print(encrypted_text)
print("\nDecrypted Text:\n")
print(decrypted_text)
verify(original_text, decrypted_text)
