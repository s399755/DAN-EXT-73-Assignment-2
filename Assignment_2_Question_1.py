# Group Name: [DAN/EXT 73]

# Group Members:
# Patrick Burzynski - [399755]

# Question 1
"""This program reads text from a file, encrypts it using a simple Caesar shift,
then decrypts it to verify the original message is correctly restored."""
# Feedback noted from assignment 1, less comments (comments only kept relevant).

# Read original text file
with open("raw_text.txt", "r") as file:
    original_text = file.read()
    
print(original_text)