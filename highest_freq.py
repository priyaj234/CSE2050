from letters import * #importing the first two assignment functions

def highest_freq(new_dict):#creating a function to find which letter has the highest frequency in a text file
    ''' This function uses the existing functions letter_count and letter_frequency and finds which letter has the highest frequency'''
    highest_val = 0 #creating a variable to hold the highest frequency
    highest_value = tuple()#creating a tuple that will hold the letter and the frequency value of the letter with the highest frequency value 
    for k in new_dict:#selecting a letter in the dictionary with letters' frequency values
        if new_dict[k] > highest_val:#determining if that letter's frequency value is higher than already stored highest frequency value
            highest_val = new_dict[k]# if it is this will store that new frequency value as the highest
            highest_value = (k,  highest_val)#this is storing that letter and its value in the created tuple
    return highest_value#returning the letter and the highest frequency value
    

#the following four lines are testing the function
expected_highest = ('a', 0.07407407)
actual_high = (highest_freq(letter_frequency(letter_count('test_file.txt'))))
actual_highest = (actual_high[0], round(actual_high[1], 8))
assert(expected_highest == actual_highest)

