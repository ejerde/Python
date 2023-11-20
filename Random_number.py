"""
Random number generator with driver code
By Eric Jerde
10/28/2023
"""

import random
''' 
import random function
'''


def guess_random_num(tries, start, stop):
    '''
    task 1 doc string: user interaction
    '''

    random_num = random.randint(start, stop)

    while tries:
        print("The number of tries left:", tries)
        guess = int(input("Please guess a number between " + str(start) + " and " + str(stop) + ":"))
        if guess == random_num:
            print("You have guessed the number correctly!")
            return random_num
        if guess < random_num: 
            print("Guess higher!")
        else:
            print("Guess lower!")
        tries -= 1

    print("You did not guess the correct number:",  random_num)
    return None


def guess_random_num_linear(tries, start, stop):
    '''
    Task 2 doc string: linear numerical search program

    '''
    random_num = random.randint(start, stop)
    print("The number to be randomly guessed is:", random_num)

    for num in range(start, stop+1, 1):

        if not tries: 
            print("The program didn't guess the right number")
            return False
        
        print("The number of tries remaining are:", tries)
        print("The program guessed:", num)

        if num == random_num:
            print("The program has guessed correctly!")
            return True
        tries -= 1


def guess_random_num_binary(tries, start, stop):
    '''
    task 3 doc string: random binary search  
    '''

    random_num = random.randint(start, stop)
    print("The program will search for a random number:", random_num)

    lower_bound = start
    upper_bound = stop

    while tries:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_num:
            print("The program has found the number!")
            return True
        if pivot > random_num:
            print(f"{pivot} Please guess a lower number")
            upper_bound = pivot - 1
        else:
            print(f"{pivot} Please guess a higher number")
            lower_bound = pivot + 1
        tries -= 1

    print( "The program could not locate the correct number.")
    return False


# Driver Code Task One
#   5 == tries
#   0, 10 == Range of random integers to choose from.


#guess_random_num(5, 0, 10)

# Driver Code Task Two
#   5 == tries
#   0, 10 == Range of random integers to choose from.

#guess_random_num_linear(5, 0, 10)

# Driver Code Task Three
#   5 == tries
#   0, 100 == Range of random integers to choose from.

guess_random_num_binary(5, 0, 100)


# Driver code for gambling game

# gambling_game()
