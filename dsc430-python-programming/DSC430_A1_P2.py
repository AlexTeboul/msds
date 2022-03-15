#Alex Teboul
#Due: 1/22/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”

import math #used in square root, ceil to round up, etc

#---------------------
#a) Write a function to return True for prime and False for not prime

def isit_prime(number):
    ''' This function returns true if an int is prime.  
    If the int is not prime or if it is an invalid input return false. The function accepts numbers only, no strings, lists, etc! '''

    if type(number) == int:                                 #first check that the input is even an int
        if number > 1:                                      #integer numbers greater than 1 can be prime
            if number == 2:                                 #weak code but it gets the sqrt part to work which is more efficient in the long run anyways
                return True                                 #2 is the first prime
            up_until_number = math.ceil(math.sqrt(number)+1)  #more efficient to check up until the square root of the prime has been passed. ex. is 113 prime, for loop would go to 11 and conclude it is prime.+1 helps with the error from going to a sqrt for low nums
            for factor in range(2,up_until_number):         #numbers from 2 to the up_until_number to see if the number you're checking is prime
                if (number % factor) == 0:                  #check if the number can be divided by the factors with no remainder
                    return False                            #it's not prime 
            else:                                           #out of line so it works for 2
                return True                                 #it's prime because no factors divide into it with no remainder
        else:
            return False                                    #it's definitely not prime because it's not an integer number greater than 1
    else:
        return False

#Test some numbers to confirm
#print(isit_prime(1), isit_prime(2), isit_prime(3), isit_prime(4), isit_prime(9), isit_prime('helloworld'), isit_prime(25))
#it works

#---------------------
#b) Write a function that returns True if an int is happy and False if it is not happy

def isit_happy(number):
    ''' This function accepts an integer number as a parameter and returns True if an int is happy 
    and False if it is not happy. A happy number is defined as a number whose squared sum of digits eventually
    equals 1 after enough iterations of a squared sum of digits loop. Returns result (which can be either True or False)'''

    if type(number) == int:     #starting with any integer
        if number >= 1:         #must be positive and greater or equal to 1
            sum_set = set()     #a set to keep track of numbers, if there's a repeat it's not happy
            while True:         #loop with exit condition so python 3 also takes while 1 but it makes less sense to readers usually
                if number == 1: #if your number is 1 or the loop turns it into one after the sum squares business then it's happy
                    return True #happy
                sum = 0         #set sum to zero in each loop at the start
                for digit in str(number):   #take your number and make it a string, then loop through the digits
                    sum += int(digit)**2    #add the square of each digit in the number to the sum variable
                number = sum                #set number equal to sum to check if it's become 1 or is a repeat
                if number in sum_set:       #so if the number has already appeared then it's sad not happy
                    return False            #sad
                sum_set.add(number)         #add the number to the set to keep track of it
    else:
        return 'Not an int / try again' #The number is not a positive integer so it's definitely not happy

#Test out some numbers to check code
#print()
#print(isit_happy(1),isit_happy(2),isit_happy(3),isit_happy(4),isit_happy(5),isit_happy(6),isit_happy(7),isit_happy(8),isit_happy(9),isit_happy(10))
#it works

#---------------------
#c) Write a function that returns true if an int is a happy prime, the int is both happy and a prime

def isit_happy_prime(number):
    ''' This function accepts a int number as its parameter and returns true if that
    int number is a happy prime. It uses the isit_prime and isit_happy functions 
    to determine it it's a happy_prime. '''
    
    p = isit_prime(number)  #p is a variable that holds True or False for prime
    h = isit_happy(number)  #h is a variable that holds True or False for happy

    if p == True and h == True: #if it's prime and happy return true
        return True             #happy prime
    else:                       
        return False            #not happy prime

#Test out some numbers to check the code
#print(isit_happy_prime(13))
#it works

#---------------------
#d)Print to the console the first 20 primes.

def n_primes(n):
    ''' Takes in a number n and returns the first n primes. '''
    count = 0               #count keeps track of how many numbers have been added to the list
    number = 0              #number is counts up by 1, basically so you can check if each positive integer number is prime or not
    n_primes_list = []      #list to hold n_primes
    while count < n:        #while the count is less than the number of primes you want to print out, keep going
        if isit_prime(number) == True:  #if a number is prime, add it to the list and increase the count of primes held in the list by 1
            count += 1
            n_primes_list.append(number)
        number += 1                     #increment number by one to keep checking if numbers are prime
    return n_primes_list                #returns the list of primes
print()
print("d) n_primes = " , n_primes(20))     #print the first 20 primes to the console
#it works

#---------------------
#e) Print to the console the first 20 happy numbers.

def n_happys(n):
    ''' Takes in a number n and returns the first n happy numbers. '''
    count = 0               #count keeps track of how many numbers have been added to the list
    number = 0              #number is counts up by 1, basically so you can check if each positive integer number is happy or not
    n_happys_list = []      #list to hold n_happys
    while count < n:        #while the count is less than the number of happys you want to print out, keep going
        if isit_happy(number) == True:  #if a number is happy, add it to the list and increase the count of happys held in the list by 1
            count += 1
            n_happys_list.append(number)
        number += 1                     #increment number by one to keep checking if numbers are happy
    return n_happys_list                #returns the list of happys
print()
print("e) n_happys = " , n_happys(20))     #print the first 20 happys to the console
#it works

#---------------------
#f) Print to the console the first 20 happy primes.

def n_happy_primes(n):
    ''' Takes in a number n and returns the first n happy primes. '''
    count = 0                       #count keeps track of how many numbers have been added to the list
    number = 0                      #number is counts up by 1, basically so you can check if each positive integer number is a happy prime or not
    n_happy_primes_list = []        #list to hold n_happy_primes
    while count < n:                #while the count is less than the number of happy primes you want to print out, keep going
        if isit_happy(number) == True and isit_prime(number) == True:  #if a number is a happy prime, add it to the list and increase the count of happy primes held in the list by 1
            count += 1
            n_happy_primes_list.append(number)
        number += 1                     #increment number by one to keep checking if numbers are happy primes
    return n_happy_primes_list          #returns the list of happy primes
print()
print("f) n_happy_primes = " , n_happy_primes(20))     #print the first 20 happy primes to the console
#it works

#---------------------
#g) Print to the console the first 20 sad primes.
def n_sad_primes(n):
    ''' Takes in a number n and returns the first n sad primes. '''
    count = 0                       #count keeps track of how many numbers have been added to the list
    number = 0                      #number is counts up by 1, basically so you can check if each positive integer number is a sad prime or not
    n_sad_primes_list = []          #list to hold n_sad_primes
    while count < n:                #while the count is less than the number of sad primes you want to print out, keep going
        if isit_happy(number) == False and isit_prime(number) == True:  #if a number is a sad prime, add it to the list and increase the count of sad primes held in the list by 1
            count += 1
            n_sad_primes_list.append(number)
        number += 1                   #increment number by one to keep checking if numbers are sad primes
    return n_sad_primes_list          #returns the list of sad primes
print()
print("g) n_sad_primes = " , n_sad_primes(20))     #print the first 20 sad primes to the console
#it works
print()
print("all done")
print()