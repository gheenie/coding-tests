def anagram_difference(w1, w2):
    # Increase a counter every time a pair of match is found.
    # Double it and subtract that from the total num of letters
    
    matched_letters_count = {}
    
    for letter1 in w1:
        matches = 0
        
        for letter2 in w2:
            if letter1 == letter2:
                matches += 1
        
        if matches > 0:
            if letter1 not in matched_letters_count:
                matched_letters_count[letter1] = 1
            elif matches > matched_letters_count[letter1]:
                matched_letters_count[letter1] += 1

    return  len(w1) + len(w2) - sum(matched_letters_count.values()) * 2 # the number of characters to remove from w1 and w2 to make them anagrams of each other


# Should print 10
print(anagram_difference('codewars', 'hackerrank'))
