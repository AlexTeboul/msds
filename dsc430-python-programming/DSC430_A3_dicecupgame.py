#Alex Teboul
#Due: 2/19/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”

#imports
import random
import math

class SixSidedDie:
    'A class that represents a six sided die. roll(), getFaceValue(), and __repr__().  '
    
    def __init__(self, rollval=1, sides = 6, classname = 'SixSidedDie'):
        'initialize the value of a roll'
        self.rollval = rollval
        self.sides = sides
        self.classname = classname
    
    def roll(self):
        'return roll - the randomly generated integer number in the range of 1 to the number of sides of the dice.'
        self.rollval = random.randint(1,self.sides)
        return self.rollval
    
    def getFaceValue(self):
        'return facevalue - the number that got randomly generated'
        return self.rollval
      
    def __repr__(self):
        'canonical string representation SixSidedDie(facevalue)'
        return '{}({})'.format(self.classname, self.rollval)

class TenSidedDie(SixSidedDie):
    'extends the SixSidedDie class to dice with 10 sides'

    def __init__(self, rollval=1, sides = 10, classname = 'TenSidedDie'):
        'initialize the value of a roll'
        self.rollval = rollval
        self.sides = sides
        self.classname = classname
    
    def __repr__(self):
        'canonical string representation TenSidedDie(facevalue)'
        return '{}({})'.format(self.classname, self.rollval)

class TwentySidedDie(SixSidedDie):
    'extends the SixSidedDie class to dice with 20 sides'
    
    def __init__(self, rollval=1, sides = 20, classname = 'TwentySidedDie'):
        'initialize the value of a roll'
        self.rollval = rollval
        self.sides = sides
        self.classname = classname
    def __repr__(self):
        'canonical string representation TwentySidedDie(facevalue)'
        return '{}({})'.format(self.classname, self.rollval)

class Cup:
    'A cup will hold several dice that may be rolled at once. The cup may hold any number of six-, ten, or twenty- sided dice. Includes: roll(), getSum(), __repr__().  '
    
    def __init__(self, numsix=1, numten=1, numtwenty=1):
        'initialize the value of a roll of the cup'
        self.numsix = numsix
        self.numten = numten
        self.numtwenty = numtwenty
        
        self.sixlist=[1]         #record each roll in list, initialize list vals to 1
        self.tenlist=[1]
        self.twentylist=[1]
        self.cuplist=[]

        self.sixsum=0           #sum of rolls so far
        self.tensum=0
        self.twentysum=0

        self.rollsum = 3        #defualt rollsum

    def roll(self):
        'return the roll of the Six, Ten, and Twenty Sided Dice in the cup.'
        self.sixlist=[]         #record each roll in list
        self.tenlist=[]
        self.twentylist=[]

        for i in range(self.numsix):
            self.sixlist.append(SixSidedDie().roll())
        self.sixsum = sum(self.sixlist)                   #sum of rolls so far
        
        for i in range(self.numten):
            self.tenlist.append(TenSidedDie().roll())
        self.tensum = sum(self.tenlist)

        for i in range(self.numtwenty):
            self.twentylist.append(TwentySidedDie().roll())
        self.twentysum = sum(self.twentylist)           
        
        self.cuplist = self.sixlist + self.tenlist + self.twentylist
        self.rollsum = self.sixsum + self.tensum + self.twentysum
        return self.rollsum
        
    def getSum(self):
        'return the sum of the rolls'
        return self.rollsum

    def __repr__(self):
        'canonical string representation Cup()'
        self.sixesformat=''
        for i in range(self.numsix):
            self.sixesformat += "SixSidedDie({}), ".format(self.sixlist[i])
            
        self.tensformat=''
        for i in range(self.numten):
            self.tensformat += "TenSidedDie({}), ".format(self.tenlist[i])
         
        self.twentysformat=''
        for i in range(self.numtwenty):
            self.twentysformat += "TwentySidedDie({}), ".format(self.twentylist[i])
        self.finish = ''
        self.finish = self.sixesformat + self.tensformat + self.twentysformat
        
        return "Cup({})".format(self.finish.rstrip(", "))



#test cases
print()
print()
print("TEST CASES:")
print()
d = SixSidedDie()
print("d>>>", d)
print("d.roll()>>>", d.roll())
print("d.getFaceValue()>>>", d.getFaceValue())
print("d>>>", d)
print()
cuptest1 = Cup()
print("cuptest1>>>", cuptest1)
print("cuptest1.roll()>>>", cuptest1.roll())
print("cuptest1.getSum()>>>", cuptest1.getSum())
print("cuptest1>>>", cuptest1)
print()
cuptest2 = Cup(0,1,1)
print("cuptest2>>>", cuptest2)
print("cuptest2.roll()>>>", cuptest2.roll())
print("cuptest2>>>", cuptest2)
print("cuptest2.getSum()>>>", cuptest2.getSum())
print("cuptest2>>>", cuptest2)
print()
print()
print()

#--------------------
print("-----------------")


def dicecupgame():
    'Play the dicecupgame where you bet on the roll of dice in a virtual cup, and win if you get the sum of the roll, or close to it.'

    #1.	Greet the user and ask their name.  
    print("Hello and welcome to the dice and cup game! May the odds be ever in your favor! Please read over the rules below.")
    print("1) Enter a username")
    print("2) Start with a Balance of $100.")
    print("3) Respond Y to play or N to Exit the game.")
    print("4) Decide how much you would like to bet. ")
    print("5) Choose how many six, ten, and or twenty sided dice you want to roll.")
    print("6) If the sum of your roll is close to enough to a random number between 1 and 100. You win!")
    print()

    username = input("Please enter your nickname (ex. AlexT): ")
    print()

    #2.	Provide the user with a balance of 100 dollars.
    balance = 100
    print('You have a balance of ${}'.format(balance))
    print()

    #3.	Ask them if they would like to play a game.
    #print('So {}, would you like to play?'.format(username))
    playgame=None
    while playgame not in ('y', 'n'):
        playgame = input("Want to play? Enter Y to continue to play, or N to Exit: ")
        playgame = playgame.lower() #accepts Y, y, N, and n
        if playgame not in ('y','n'):
            print("You must enter either a Y or an N, try again...")
    print()

    while balance > 0:
        if playgame == 'n':
            print('You typed N and have been exited from the game')
            break
        elif playgame == 'y':

            #4.	Generate a random number between 1 and 100.  This number will be called the goal.
            goal = random.randint(1,100)
            print("The goal for this round is {}.".format(goal))
            #print("The goal for this round is has been generated. It is a random integer number between 1 and 100.")
            print("If the sum of dice rolled equals this value you receive 10x your bet, within 5 then 5x your bet, within 10 then 2x your bet. Otherwise you lose.")
            print()

            #5.	Ask the user how much they would like to bet.
                #bet can't be a zero
                #bet can't be a string
                #bet can't be negative
                #bet can't be more than balance

            while True:
                try:
                    bet = float(input("How much would you like to bet?: "))
                    #bet = round_down(bet,2)
                    bet = (math.floor(bet * 100)) / 100.0
                    if bet > balance:
                        print('The bet was greater than the balance. Try Again...')
                    elif bet <= 0:
                        print('The bet was less than or equal to zero. Try Again...')
                    elif type(bet) == str:
                        print('You entered a string. Has to be an int. Try Again')
                    else:
                        print('This is an acceptable bet.')
                        break
                except:
                    print('You did not enter a valid bet. Make sure you enter a number (ex. 10.25). Try Again...')

            while True:
                #6.	Ask the user how many of each die they would like to roll.
                    #can't be negative
                    #don't want a crazy number of dice. They can't win with over 110 dice rolled.
                    #can't be strings
                try:
                    print("Please enter how many 6, 10, and/or 20 sided dice you would like to roll.")
                    num_6sides = eval(input("How many 6-sided dice would you like to roll (ex. 1): "))
                    num_10sides = eval(input("How many 10-sided dice would you like to roll (ex. 1): "))
                    num_20sides = eval(input("How many 20-sided dice would you like to roll (ex. 1): "))
                    if num_6sides < 0 or num_10sides < 0 or num_20sides < 0:
                        print('At least one dice selection you made was negative. Try Again...')
                    elif type(num_6sides)==float or type(num_10sides)==float or type(num_20sides)==float:
                        print('Float Entered Error. You have to enter an integer (whole number) of dice (ex. 4). Try Again...')
                    elif type(num_6sides)==str or type(num_10sides)==str or type(num_20sides)==str:
                        print('String Entered Error. You have to enter an integer (whole number) of dice (ex. 4). Try Again...')
                    elif (num_6sides + num_10sides + num_20sides) > 110:
                        print('You placed over 110 dice in the cup. This is a bad move, use less dice! Try Again...')
                    elif (num_6sides + num_10sides + num_20sides) == 0:
                        print('You placed no dice in the cup. Try Again...')
                    else:
                        print('This is an acceptable set of dice.')
                        print()
                        break
                except:
                    print('You did not enter a valid bet. Try Again...')

            #7.	Create a cup filled with dice according to the user’s input.
            cup = Cup(num_6sides, num_10sides, num_20sides)

            #8.	Roll the cup and display the results.
            cup.roll()
            cupsum = cup.getSum()
            print("Your roll was: {}".format(cup))
            print("You rolled a sum of {} ".format(cupsum))

            #difference between cupsum and the goal
            difference = abs(goal - cupsum)

            #9.	If the roll exactly matches the goal the user receives 10x bet added to their balance.
            if difference == 0:
                balance = 10*bet + balance
            #10. Otherwise, if the roll is within 5 of the goal but not over the user receives 5x bet added to their balance.
            elif difference <= 5:
                balance = 5*bet + balance
            #11. Otherwise, if the roll is within 10 of the goal but not over the user receives 2x bet added to their balance
            elif difference <=10:
                balance = 2*bet + balance
            #otherwise they lose their bet and it gets subtracted from their balance.
            else:
                balance -= bet

            #12. Report the results to the user.  The message should include their name and updated balance.
            results = "Hey {}, your new balance is {}. You bet ${} and the goal was {}. You rolled {}, giving you a difference of {}.".format(username, balance, bet, goal, cupsum, difference)
            print(results)
            if balance == 0:
                print("You're all out of dough. Balance = 0. You will be exited from the game now.")
                break

            #13. Ask if they would like to play again.  If so go to step 3.
            playagain = None
            while playagain not in ('y', 'n'):
                playagain = input("Would you like to play again? Enter Y to play again, or N to Exit: ")
                playagain = playagain.lower() #accepts Y, y, N, and n
                if playagain not in ('y','n'):
                    print("You must enter either a Y or an N. Try again...")
                elif playagain == 'n':
                    print("You entered N and have been exited from the game")
                    return
                else:
                    playgame = playagain

dicecupgame()



