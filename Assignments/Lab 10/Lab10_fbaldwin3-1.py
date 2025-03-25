def word_frequency(content):
    frequency = {}

    # Define punctuation characters
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    # Remove punctuation, make lowercase, and strip whitespace
    for character in punctuation_characters:
        content = content.replace(character, "").lower().strip()

    # Split the file into words
    words = content.split()

    # Count word occurrences
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

def print_words(frequency):
    # Print words alphabetically and their counts
    for word in sorted(frequency.keys()):
        print(word, frequency[word])

def main():
    try:
        # Get the filename from the user
        filename = input("Enter the filename: ")

        # Read the file content
        file = open(filename, "r")
        content = file.read()
        file.close()

        # Call word frequency function
        word_data = word_frequency(content)

        # Call print function
        print_words(word_data)

    except:
        print(f"File {filename} cannot be read.")

main()