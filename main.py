import os
from collections import Counter

#Open text file
file = open("LOCATIONHERE", "r")
text = file.read()  #Read the file content as a string
file.close() #Close after reading file

#Filter text to remove spaces, and make all characters lowercase
def filter_text(text):
    #Replace spaces and make lowercase
    filtered_text = text.replace(' ', '').lower()
    return filtered_text

#Count characters in filtered text string
def countchr(filtered_text):
    # Use Counter to count occurrences of each alphanumeric character
    counter = Counter(char for char in filtered_text if char.isalnum())
    return counter

#Filter the text and count the characters
filtered_text = filter_text(text)
char_count = countchr(filtered_text)

#List the count of each character a-z, 0-9
for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")
