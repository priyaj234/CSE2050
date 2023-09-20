import time

def find_pairs_naive(all_num = [1, 2, 3, 4, 5], target_num = 5):
    '''This function takes in a list of numbers and a target number and returns a set of pairs of numbers from the original list that
     sum to equal the target number, but this one doesn't focuse on the time complexity of the function.'''
    set_of_pairs = set()
    if all_num == []:                                             #1
        raise IndexError("The input list is empty")
    elif target_num == 0:                                         #1
        return {}
    else:                                                         #1
        for first_num in all_num:                                         #n
            for second_num in all_num:                                     #n
                if first_num + second_num == target_num:                           #1
                    set_of_pairs.add((first_num, second_num))                      #1
                    all_num.remove(first_num)                             #1
                    all_num.remove(second_num)                             #1
        return set_of_pairs                                       #1
                                                                  #-----
                                                                  #(1+1+1) + n*n(1+1+1+1+1) + 1= 5n^2 + 4 = O(n^2)
                                                                  #The big O analysis shows that the algorithm is a quadratic function so it can be denoted by O(n^2) 

def find_pairs_optimized(all_num = [1, 2, 3, 4, 5], target_num = 5):
    '''This function takes in a list of number and a target number and returns a set of pairs of numbers from the original list that 
    sum to equal the target number, but unlike the previous function find_pairs_naive, it focuses on make the function run faster using 
    time complexity'''
    all_num_list = set(all_num)
    set_of_pairs = set()
    if all_num == []:                                            #1
        raise IndexError("The input list is empty")
    elif target_num == 0:                                        #1
        return {}
    else:                                                        #1
        for first_num in all_num:                                        #n
            if target_num - first_num in all_num_list:                   #1
                if (target_num - first_num, first_num) not in set_of_pairs:      #1
                    if target_num - first_num != first_num:                      #1
                        set_of_pairs.add((first_num, target_num - first_num))    #1
        return set_of_pairs                                      #1
                                                                 #-----
                                                                 # (1+1+1) + n(1+1+1+1) + 1 = 4n + 4 = O(n)
                                                                 #The big O analysis shows that the algorithm is a linear function so it can be denoted by O(n)



def measure_min_time(fn, args, n = 10):
    '''This function takes in another function, its arguments, and a number of times to run and returns the run time of the fastest run.'''
    current_min = float('inf')
    for num in range(n):
        start = time.time()
        fn(*args)
        end = time.time()
        if end - start <= current_min:
            current_min = end - start
    return current_min

if __name__ == "__main__":
    lst = list(range(0, 1000))
    print(" n          naive      optimized")
    print("********************************")
    for n in[10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        print (f" {n}     {measure_min_time(find_pairs_naive, (lst, 101) , n):.4f}     {measure_min_time(find_pairs_optimized, (lst, 101), n):.4f}")
    print("--------------------------------")


