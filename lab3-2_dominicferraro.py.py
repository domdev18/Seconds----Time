#Dominic Ferraro; Lab 3-1; 9-6-22
#This program does the following:
#prompts the user to enter any amount of seconds
#the program uses a series of if statments to determine what calulation to use
#prints the amount of seconds entered into day, hour, minute, and seconds
#=============================================================variables declared
import math
minute = float(60)
hour = 3600
day = 86400
seconds = minuteAns = secondAns = hourAns = dayAns = float(0)
#==============================================================input statements
seconds = float(input(('enter a number of seconds ')))
#============================================================calculation statements

if seconds >= minute and seconds < hour:
    minuteAns = math.floor(seconds/minute)
    time = seconds/minute
    secondAns = math.ceil((time - minuteAns)*60)
    print(minuteAns, 'minutes and ',secondAns,'seconds')

if seconds >= hour and seconds < day:
    hourAns = math.floor(seconds/hour)
    time = (seconds/hour)- hourAns
    minuteAns = math.floor((time * 60))
    secondAns = seconds - (hourAns * hour) - (minuteAns * minute)

if seconds >= day:
    dayAns = math.floor(seconds/day)
    time = seconds/day 
    hourAns = math.floor((time - dayAns)*24)
    time = seconds/hour
    minuteAns = math.floor((seconds - ((dayAns * day) + (hourAns * hour)))/minute)
    secondAns = seconds - (dayAns * day) - (hourAns * hour) - (minuteAns * minute)
    print('seconds entered:',seconds)
    print(dayAns, 'days and ', hourAns,'hours and ',minuteAns, 'minutes and ',secondAns,'seconds');  
if seconds < minute:
    print('seconds entered:',seconds)
    print(seconds,'seconds')
#==============================================================output statements

