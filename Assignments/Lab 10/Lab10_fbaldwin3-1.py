import string


def word_frequency(file):
    frequency = {}

    # Define punctuation characters to remove
    punctuation_chars = string.punctuation

    # Read the first line of the file
    line = file.readline()

    while line:
        # For each punctuation character, remove it from the line
        for punctuation in punctuation_chars:
            line = line.replace(punctuation, "")

        # Split the line into individual words
        words = line.split()

        # For each word in the line
        for word in words:
            # Convert the word to lowercase for case-insensitive counting
            lowercase_word = word.lower()

            # Add the word to the dictionary, or update its count if already present
            frequency[lowercase_word] = frequency.get(lowercase_word, 0) + 1

        # Read the next line from the file
        line = file.readline()

    # Return the frequency dictionary
    return frequency

def print_words(data):
    # Print each word and its respective count, sorted alphabetically
    for word in sorted(data.keys()):
        print(word, data[word])

def main():
    try:
        # Get the filename from the user
        filename = input("Enter the filename: ")

        # Read file
        with open(filename, "r") as file:
            content = file.read()

        word_data = word_frequency(content)

        print_words(word_data)

    except:
        print(f"The file {filename} is not readable.")

main()