import os
from collections import Counter
import unicodedata

#Load text file
file = open("LOCATIONHERE", "r", encoding="utf-8") #Set .txt file location
text = file.read()  #Read the file content as a string
file.close() #Close the file

#Filter text to better count characters
def filter_text(text):
    normalized_text = unicodedata.normalize('NFKC', text)
    #Remove spaces
    filtered_text = ''.join(normalized_text.split())
    return filtered_text

#Count characters in filtered text string
def countchr(filtered_text):
    counter = Counter(filtered_text)
    return counter

#Filter text and count characters
filtered_text = filter_text(text)
char_count = countchr(filtered_text)

#List the sorted count of each character
for char in sorted(char_count):
    print(f"{char} (U+{ord(char):04X}): {char_count[char]}")