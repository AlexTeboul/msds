#Alex Teboul
#Due: 2/5/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”
import os

def name_ending_counter(datafile_boys, datafile_girls):
    ''' This function accepts the names of two datafiles (FULL PATH) of child names as parameters and returns a printed count of the number
    of times a letter a-z appears at the end of the names in the datafiles.'''

    #turn the two datafiles into lists / read in the files
    boys_file = open(datafile_boys, 'r')        #read in the boys file
    boys_list = boys_file.readlines()           #readlines gets each name in the list
    boys_list = list(map(str.strip, boys_list)) #this removes the pesky \n
    boys_file.close()                           #always close

    girls_file = open(datafile_girls, 'r')      #same for the girls
    girls_list = girls_file.readlines()
    girls_list = list(map(str.strip, girls_list))
    girls_file.close()
  
    #keep only the last letter of each name
    boys_end_chars = []                 #empty list that will hold last letters of boys names
    for name in boys_list:
        boys_end_chars.append(name[-1]) #-1 is the last letter in the names
    boys_end_chars.sort()               #alphabetize it

    girls_end_chars = []                #same for girls (i know it's repetitive code but -\_''_/-  )
    for name in girls_list:
        girls_end_chars.append(name[-1]) 
    girls_end_chars.sort()

    letter_set = set()                              #empty set for all the letters that appear in boys and girls name endings
    char_list = boys_end_chars + girls_end_chars    #list of all endings
    for letter in char_list:                        
        letter_set.add(letter)                      #make set of endings
    endings_list = list(letter_set)                 #turn set into list
    endings_list.sort()                             #sort the list alphabetically

    #make a dict counter
    boys_counter = {}                   #dictionary to count letter frequency
    for letter in boys_end_chars:   
        if letter in boys_counter:      #counter for letter already in dict
            boys_counter[letter] += 1   #increment by 1
        else:                           #counter for letter not in counter yet
            boys_counter[letter] = 1    #set to 1 for first

    girls_counter = {}                  #same for girls
    for letter in girls_end_chars:   
        if letter in girls_counter:
            girls_counter[letter] += 1
        else:                
            girls_counter[letter] = 1
    
    #print to the console
    print('{0:<8}{1:<8}{2:<8}'.format('Letter', 'Boys', 'Girls'))   #first line column headers
    for letter in endings_list:                                     #get those counts printed to the console
        if letter in boys_counter and letter in girls_counter:
            print('{0:<8}{1:<8}{2:<8}'.format(letter, boys_counter[letter],girls_counter[letter]))
        elif letter in boys_counter and letter not in girls_counter:
            print('{0:<8}{1:<8}{2:<8}'.format(letter, boys_counter[letter],'0'))
        elif letter in girls_counter and letter not in boys_counter:
            print('{0:<8}{1:<8}{2:<8}'.format(letter,'0',girls_counter[letter]))
        else:
            print('{0:<8}{1:<8}{2:<8}'.format(letter,'missing','missing')) #in case some weird error occurs
    print()
    
    return 

#not sure how you wanted the directory set up so the function takes in the full path.
#directory_path = '/Users/alexteboul/Desktop/'
directory_path = input('Please enter the path for namesBoys.txt and namesGirls.txt in the form /Users/alexteboul/Desktop/: ')
name_ending_counter(directory_path + 'namesBoys.txt', directory_path + 'namesGirls.txt')

#Interesting finds paragraph:
    #The majority of girls names end in a (380 times), while boys names mostly end in n (340 times).
    #Q is the only letter that no names end in. INTERESTING!
    #More girls names end in vowels than boys names do. 603 girls names end in vowels (aeiou) while
    #only 207 boys names end in vowels. That's about 3 times as often a girl's name will end in
    #a vowel than a boy's name. That also means more boys names end in consonants than girls names do.