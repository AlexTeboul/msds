#Alex Teboul
#Due: 2/5/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”

#I didn't include error handling try/exception.. assuming correct points will be entered for testing/grading
#on this problem just because question didn't ask for it.

def ellipse_area():
    ''' This function asks the user to enter the x and y coordinates 
    for the two focal points of the ellipse, the length of the major axis and 
    the number of random points to employ.  The program then computes and prints 
    the area of the ellipse.'''
    #imports
    import random
    import math

    print('Welcome!')
    print()
    print('This program will use random numbers to compute the area of an ellipse.')

    #User Inputs
    F1_string = input('Enter the position of F1 (format: x y): ')
    F2_string = input('Enter the position of F2 (format: x y): ')
    major_axis = int(input('Enter the length of the major axis (format: l): '))
    num_random = int(input('Enter the number of random points (format: n): '))
    print('Thinking...')

    #formatting 
    F1_stringlist = F1_string.split(" ") #space in between coordinates entered
    F1_list = list(map(int, F1_stringlist))
    F2_stringlist = F2_string.split(" ") #space in between coordinates entered
    F2_list = list(map(int, F2_stringlist))

    #Bounding Box
    x_left = min(F1_list[0],F2_list[0]) - major_axis
    x_right = min(F1_list[0],F2_list[0]) + major_axis
    y_bottom = min(F1_list[1],F2_list[1]) - major_axis
    y_top = min(F1_list[1],F2_list[1]) + major_axis
    area_bounding_box = (x_right-x_left)*(y_top-y_bottom)


    #In or out
    in_ellipse_count = 0
    notin_ellipse_count = 0
    for i in range(num_random):
        x = round(random.uniform(x_left, x_right),1) #1 decimal place like the word doc example for user input
        y = round(random.uniform(y_bottom, y_top),1)
        distance_to_F1 = math.sqrt( (F1_list[0]-x)**2 + (F1_list[1]-y)**2 )
        distance_to_F2 = math.sqrt( (F2_list[0]-x)**2 + (F2_list[1]-y)**2 )
        dist_sum = distance_to_F1 + distance_to_F2
        if dist_sum <= major_axis:
            in_ellipse_count += 1
        else:
            notin_ellipse_count += 1

    percentage_ellipse = in_ellipse_count/num_random
    area_ellipse = percentage_ellipse * area_bounding_box

    result = print('The area of the ellipse is approximately {}'.format(area_ellipse))
   
    return result

#run the function / user gets asked for inputs / etc
ellipse_area()
