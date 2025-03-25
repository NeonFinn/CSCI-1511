# Finn Baldwin, 3/25/25, Lab 10 - Count word frequency in a file from user input
import os

def word_frequency(content):
    frequency = {}

    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    # Remove punctuation, make lowercase, and strip whitespace
    for character in punctuation_characters:
        content = content.replace(character, "").lower().strip()

    words = content.split()

    # Count word occurrences
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

def print_words(frequency):
    for word in sorted(frequency.keys()):
        print(f"{word} - {frequency[word]}")

def main():
    try:
        filename = input("Enter the filename to process: ")

        # Read the file content then close the file
        file = open(filename, "r")
        content = file.read()
        file.close()

        # Call word frequency function to assign to data
        word_data = word_frequency(content)

        # Call print function
        print_words(word_data)

        # Keep file open
        input()

    except:
        print(f"File {filename} cannot be read. Press enter to exit.")
        input()
        os.close(1)

main()