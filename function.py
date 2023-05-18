def most_frequent(string):
    # Create an empty dictionary to store the letter frequencies
    frequency = {}

    # Count the frequency of each letter in the string
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    # Sort the letters based on their frequencies in descending order
    sorted_letters = sorted(frequency, key=frequency.get, reverse=True)

    # Print the letters in decreasing order of frequency
    for letter in sorted_letters:
        print(letter, frequency[letter])

# Example usage
most_frequent("Mississippi")
