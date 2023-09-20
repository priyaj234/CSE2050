from math import log2


def linear_scan(L):
    '''A function to scan through a list and test for any possible edge cases'''
    already_sorted = True #assuming the list already sorted
    reverse_of_list = True #assuming the list sorted, but just reversed
    out_of_place_count = 0 #assuming there is nothing out of place
    
    for i in range(len(L)-1): #iterating through the entire list
        if L[i] > L[i+1]: #if even one is out of place then it isn't sorted and 1 is added to the count of ones that are out of place
            already_sorted = False
            out_of_place_count += 1
        elif L[i] < L[i+1]: #if even one isn't in reverse order it isn't in reverse
            reverse_of_list = False
        
    if already_sorted:
        return "Sorted"
    elif reverse_of_list:
        return "Reverse"
    elif out_of_place_count <= 5:
        return "Insertion"
    else:
        quicksort(L)
        return "Quick"

def reverse_list(L):
    '''A function to reverse a list in place'''
    return L[::-1] #indexing through the list and reversing
    
def insertionsort(L, left, right):
    '''using insertion sorting, moving values into their correct place one at a time, to organize the list'''
    if right is None:
        right = len(L)
    for i in range(left + 1, right): #iterating from the second item in the list to the last
        compare = L[i] #setting a variable to compare to that is equal to the value of the index being iterated over
        j = i - 1 #setting the index before the one being currently checked
        while j >= left and L[j] > compare: #if the previous index is left or greater, so not less than 0, and the value of that index is greater than the one after
            L[j+1] = L[j] #the current index ends up being set to the value of the previous, so that the higher one is moved up
            j-= 1 #decrements j so the next one can be checked
        L[j+1] = compare # if the value of j is less than the next one, i, it is set to the value stored in index i
    return L


def quicksort(L, left = 0, right = None, types = set(), current_depth = 0):
    '''a function that uses quicksort on larger lists, until a certain recursion depth is reached, and then uses mergesort. If there is less than 16 items in the list 
    it automatically uses insertion sort'''
    current_depth += 1 #the depth at the start of quicksort
    if right is None:#defining right with a number
        right = len(L)
    if right - left <=16: #going into insertionsort automatically if there is 16 or less items in the list
        types.add('Insertion')
        insertionsort(L, left, right)
        return L
    elif current_depth > log2(len(L))+1: #going into mergersort if the maximum recursion depth is reached
        types.add('Mergesort')
        return mergesort(L, left, right)
    else: #calling quicksort recursively
        types.add('Quicksort')
         #Divide!
        mid = partition(L, left, right, current_depth)
        # Conquer!
        quicksort(L, left, mid, types, current_depth)
        current_depth -= 1
        quicksort(L, mid+1, right, types, current_depth)
        current_depth -= 1

    #return types

def partition(L, left, right, current_depth):
    '''helper function for quicksort'''
    pivot = right - 1
    i = left # index in left half
    j = pivot - 1 # index in right half
    while i < j:
    # Move i to point to an element >= L[pivot]
        while L[i] < L[pivot]:
            i = i + 1
        # Move j to point to an element < L[pivot]
        while i < j and L[j] >= L[pivot]:
            j = j - 1
    # Swap elements i and j if i < j
        if i < j:
            L[i], L[j] = L[j], L[i]
    # Put the pivot in place.
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return i

def mergesort(L, left = 0, right = None):
    '''the function to sorts a list using merge sort'''
    if right is None: #sets right to an integer value equaling the length of the list
        right = len(L)

    if right - left <= 16: #defaulting to insertionsort if the length of the list is 16 or less items
        insertionsort(L, left, right)
        return L
    if len(L) < 2: #doesn't sort the list if it is less than 2 items in the list
        return L
# Divide!
    mid = len(L) // 2 #setting the parmeters needed for the merge helper functions
    left = L[:mid]
    right = L[mid:]
    # Conquer!
    mergesort(left) #calling mergesort recursively on both sides
    mergesort(right)
# Combine!
    merge(left, right, L) 


def merge(left, right, L):
    '''a helper function for mergesort'''
    i = 0 # index into left
    j = 0 # index into right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i = i + 1
        else:
            L[i+j] = right[j]
            j = j + 1
        # Add any remaining elements once one list is empty
    L[i+j:] = left[i:] + right[j:]
    
   
def magic_sort(L, left = 0, right = None): 
    '''A function that using linear scan and decides which sorting algorithm to use and returning a set with the sorting algorithms used'''
    x = linear_scan(L)
    if x == "Sorted": 
        types = {'Sorted'}
        return types
    elif x == "Insertion":
        insertionsort(L, left, right)
        types = {'Insertion'}
        return types
    elif x == "Reverse":
        reverse_list(L)
        types = {'Reversed'}
        return types
    elif x == "Quick":
        types = {'Quicksort'}
        quicksort(L,0,None,types)
        return types