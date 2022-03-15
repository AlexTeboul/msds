#Alex Teboul
#Due: 1/22/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”  


def overlap(square_1, square_2):
    ''' This function calculates the overlap area between two squares on a grid.
    It accomplishes this by finding the width and height of the overlap area and 
    multiplying these values together to find area. 
    It takes in two lists as parameters. These lists have the format: 
    [x, y, side_length], where x and y are the coordinates of the lower left corner of a square 
    and side_length is the length of each side of the square. '''

    overlap_width = min(square_1[0] + square_1[2], square_2[0]+square_2[2]) - max(square_1[0], square_2[0])     #this calculates the width of the overlap between squares
    overlap_height = min(square_1[1] + square_1[2], square_2[1]+square_2[2]) - max(square_1[1], square_2[1])    #this calculates the height of the overlap between squares
    overlap_area = overlap_width * overlap_height       #overlap_area is the width times the height of overlap

    if overlap_width > 0 and overlap_height > 0:        #if both width and height overlap values are positive, that means there is overlap
        return overlap_area                             #function returns the area of overlap
    else:                                               #if the values are not positive, then there's no overlap
        return 0                                        #return 0 because there is zero overlap




#Test the Code:

totalScore = 0

S1 = [1,5,3]
S2 = [5,6,2]
S3 = [2,1,2]
S4 = [9,6,2]
S5 = [7,2,3]
S6 = [3,2,5]
S7 = [5,3,1]

#---------- ---------- ---------- ---------- ----------
print( "Test 1: " + str(S1) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S1,S6)
r2 = overlap(S6,S1)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1
    
#---------- ---------- ---------- ---------- ----------
print( "Test 2: " + str(S2) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S2,S6)
r2 = overlap(S6,S2)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 3: " + str(S3) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S3,S6)
r2 = overlap(S6,S3)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 4: " + str(S4) + str(S6) )
print( "Correct Answer: 0" )
r1 = overlap(S4,S6)
r2 = overlap(S6,S4)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 0:
    s1 = s1 + 1
if r2 == 0:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 5: " + str(S5) + str(S6) )
print( "Correct Answer: 3" )
r1 = overlap(S5,S6)
r2 = overlap(S6,S5)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 3:
    s1 = s1 + 1
if r2 == 3:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 6: " + str(S6) + str(S6) )
print( "Correct Answer: 25" )
r1 = overlap(S6,S6)
r2 = overlap(S6,S6)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 25:
    s1 = s1 + 1
if r2 == 25:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 7: " + str(S7) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S7,S6)
r2 = overlap(S6,S7)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print ( "Total Score: " + str(totalScore) )
print ( "Percentage: " + str(100*totalScore/14) )
