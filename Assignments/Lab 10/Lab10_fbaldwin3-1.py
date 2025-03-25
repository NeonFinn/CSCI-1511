def word_frequency(content):
    frequency = {}

    # Define which characters to remove
    punctuation_characters = ".,;:!?\"'()[]{}"

    # Remove punctuation and convert to lowercase
    while True:
        for character in punctuation_characters:
            content = content.replace(character, "").lower()
        break

    # Split the content into words
    words = content.split()

    # Count word occurrences
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

def print_words(frequency):
    # Print words and their counts, sorted alphabetically
    for word in sorted(frequency.keys()):
        print(word, frequency[word])

def main():
    try:
        # Get the filename from the user
        filename = input("Enter the filename: ")

        # Read the file content
        with open(filename, "r") as file:
            content = file.read()

        # Process word frequency
        word_data = word_frequency(content)

        # Print the results
        print_words(word_data)

    except:
        print(f"File {filename} cannot be read.")

main()