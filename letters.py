def letter_count (file):#creating the letter_count function
    ''' This function takes a text file and counts how many times a letter appears in the text file.'''
    with open(file, 'r') as f: #opening the file being used as a function parameter
        text = f.read().replace('\n', '') #removing the newlines so it is one continuous string
    valid_char = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}#set of valid characters for the letter count
    document = dict() #creating the dictionary where the letters and their counts will be stored
    for i in text.lower(): #selecting a word in the entirety of the text, and making the uppercase letters lowercase
        for j in i: #selecting a letter in that word
            if j in valid_char: #determing if that letter is a valid character
                if j in document: #if that character has already been added to the dictionary and one to the count
                    document[j] += 1
                else:#adding a new character to the dictionary
                    document[j] = 1
       

    return document #returning the created dictionary as the function return
    f.close()#closing the file that was opened

#the following three lines are just testing the letter_count funtion
expected_count = {"a": 2, "b": 1 , "c": 1, "d": 1, "e": 1 , "f": 1 , "g": 1 , "h": 1 , "i": 1 , "j": 1 , "k": 1 , "l": 1 , "m": 1 , "n": 1 , "o": 1 , "p": 1 , "q": 1, "r": 1 , "s": 1 , "t": 1 , "u": 1 , "v": 1, "w": 1 , "x": 1, "y": 1, "z": 1 }
actual_count = letter_count('test_file.txt')
assert(expected_count == actual_count)

def letter_frequency(document):#creating the letter_frequency function
    '''This function takes a text file and the letter_count function as input and uses the dictionary with 
    how many times a letter appears in the text file and forms a new dictionary with the frequency/rates.'''
    total = 0 #creating a variable to find the total letter count 
    new_dict = dict() #creating a new dictionary to store the frequency the letter appear at instead of the number of times
    for k in document: #choosing a letter that is in the dictionary of counts
        y = document[k] # creating a variable for the letter selected's value
        total += y #adding the selected letter's value to the total
    for k in document:#choosing a letter that is in the dictionary of counts
        new_dict[k] = document[k]/total#for the selected letter adding a frequency value, the letter's count divided by the total count, into the new dictionary
    return new_dict#returning the new dictionary that has frequency values instead of the count values

#the remaining lines were all used for testing
expected_letter_freq = {"a": 0.07407407, "b": 0.03703704 , "c": 0.03703704 , "d": 0.03703704, "e": 0.03703704 , "f": 0.03703704 , "g": 0.03703704 , "h": 0.03703704 , "i": 0.03703704 , "j": 0.03703704 , "k": 0.03703704 , "l": 0.03703704 , "m": 0.03703704, "n": 0.03703704 , "o": 0.03703704 , "p": 0.03703704 , "q": 0.03703704 , "r": 0.03703704 , "s": 0.03703704 , "t": 0.03703704 , "u": 0.03703704 , "v": 0.03703704 , "w": 0.03703704 , "x": 0.03703704, "y": 0.03703704, "z": 0.03703704 }
actual_letter_freq = letter_frequency(letter_count('test_file.txt'))
for k in actual_letter_freq:#for loop was created to round the frequency values being found by the function to say number of float digits as the expected frequencies
    actual_letter_freq[k] = round(actual_letter_freq[k], 8)
assert(expected_letter_freq == actual_letter_freq)

