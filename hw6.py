# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L): 
    '''Finds the index where the value is equal to zero'''
    left = 0 #sets left index to 0 , first index
    right = len(L) - 1 #sets last index
    median = (right + left) // 2 #finds the midpoint of the last and first index
    while L[median] != 0 and right != (left + 1): #until the median isn't the first index and the right index isn't the previously test left index
        if L[median] < 0: #checking that the value of the median is less than 0
            left = median #sets the median as the left value if median is less than 0
        elif L[median] > 0: #checking that the value of the median is greater than 0
            right =  median #sets the median as the right value if the median is less than 0
        median = (right + left) // 2 #updates the median in the for loop
    
    if L[median] == 0: #when the median is 0 then just return the median index
        return median
    else:
        return right #if not return the right index as the median
  
def bubble(L, left, right): 
    '''using bubble sorting, switching the values until reaching the correct order, to organize the list'''
    for j in range((right-1)- left): #checking every item in the list
        for i in range(left, (right-1)-j): #going from first item to last item
            if L[i]>L[i+1]: #checking if the current item is larger than the one after it
                L[i], L[i+1] = L[i+1], L[i] #
    
def selection(L, left, right): 
    '''using selection sorting, choosing the smallest values in each iteration of a list and moving it to the front if it is smaller than the previous iteration, to organize the list'''
    for i in range(left, right-1): #checking every item in the list
        min_index= i #setting the minimum index, to the one being tested 
        for index in range(i + 1, right): #checking every item from the one after the first item to the last item
            if L[index] < L[min_index]: #checking if the value of the the index is less than the value of the minimum index 
                min_index = index #updating the minimum_index if the current index is less
        L[i], L[min_index] = L[min_index], L[i] #switching the order of the index and the minimum, so the minimum comes before


def insertion(L, left, right):
    '''using insertion sorting, moving values into their correct place one at a time, to organize the list'''
    for i in range(left + 1, right): #iterating from the second item in the list to the last
        compare = L[i] #setting a variable to compare to that is equal to the value of the index being iterated over
        j = i - 1 #setting the index before the one being currently checked
        while j >= left and L[j] > compare: #if the previous index is left or greater, so not less than 0, and the value of that index is greater than the one after 
            L[j+1] = L[j] #the current index ends up being set to the value of the previous, so that the higher one is moved up
            j-= 1 #decrements j so the next one can be checked
        L[j+1] = compare # if the value of j is less than the next one, i, it is set to the value stored in index i

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half