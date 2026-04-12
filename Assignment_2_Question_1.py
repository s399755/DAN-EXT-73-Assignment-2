# Group Name: [DAN/EXT 73]

# Group Members:
# Patrick Burzynski - [399755]

# Question 1
"""This program reads text from a file, encrypts it using a simple Caesar shift,
then decrypts it to verify the original message is correctly restored."""
# Feedback noted from assignment 1, less comments (comments only kept relevant).

#Input
Shift1 = int(input("Enter shift1:")
Shift2 = int(input("Enter shift2:")

# Encrypt
def encrypt(text):
    result = ""

    for char in text:
        #lowercase letters
        if 'a' <= char <= 'z':
            if char <= 'm':
                shift = shift1 * shift2
                result += '0' +chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                shift = shift1 + shift2  
                result += '1' +chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        #uppercase letters
         if 'A' <= char <= 'Z':
            if char <= 'M':
                shift = shift1 * shift2
                result += '2' +chr((ord(char) - ord('a') - shift) % 26 + ord('A'))
            else:
                shift = shift1 + shift2  
                result += '3' +chr((ord(char) - ord('a') + shift) % 26 + ord('A'))

        # non-letters unchanged
         else:
             result += char

    return result 

#Decrypt 
def decrypt(text):
    result = ""
    i = 0

    while i < lec(text):

        if text[i] in "0123":
            marker = text[i]
            char = text[i + 1]

            if marker == "0":
                shift = shift = shift1 * shift2
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            elif marker == "1":
                shift = shift1 + shift2 
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            elif marker == "2":
                shift = shift1 + shift2 
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            elif marker == "3":
                shift = shift1 + shift2 
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            i += 2

        else: 
            result += test[i]
            i += 1 
    
    return result 
    
# Read original text file
with open("raw_text.txt", "r") as file:
    original_text = file.read()
    
print(original_text)
