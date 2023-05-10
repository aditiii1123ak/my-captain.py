def most_frequent(string):
    # create an empty dictionary
    freq_dict = {}
    
    # iterate through each character in the string
    for char in string:
        # if the character is already in the dictionary, increment its count
        if char in freq_dict:
            freq_dict[char] += 1
        # otherwise, add the character to the dictionary with a count of 1
        else:
            freq_dict[char] = 1
    
    # sort the dictionary by value in descending order and convert it to a list of tuples
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    # iterate through the list of tuples and print the characters in decreasing order of frequency
    for item in sorted_dict:
        print(f"{item[0]} = {item[1]:02d}")

most_frequent()
