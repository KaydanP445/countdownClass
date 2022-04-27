# Name: Kaydan Phipps
# Date: 4/27/2022
# Project: Countdown Timer using Github
# File: Countdowntimer --> main.py
#-----------------------------------------------------------------

import time

'''The timercountdown function is used to import the userTime parameter. This will take the seconds and translate it to a timer to allow the user to countdown.'''

def timerCountdown(userTime):
    while userTime:# start the while loop
        min, secs=divmod(userTime, 60) #divmode() function used for two variables. Min and seconds by using the user input and dividing it by 60

        timer = '{:02d} : {:02d}'.format(min, secs) #Once we identify the min and seconds through the divmode(), we can use them to set our timer accordingly in a proper format
        print('\r', timer, end=' ')#prints the timer using carriage return

        time.sleep(1)#uses the sleep function from the time library to create a one-second delay

        userTime-=1#Takes the userTime and subtracts one from the total for each second
    print('\n Timer Completed')#this prints on a new line timer completed. Once the timer runs out of the second provided

userTime = input('Please enter the time in seconds: \n')

timerCountdown(int(userTime)) #Calls the timer countdown function
#Convert the userTime string into an integer and then push it through the parameter

