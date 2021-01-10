'''
Author: shamo0

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
'''
#!/bin/python3

import os
import sys

def timeConversion(s):
    amOrPm = s[-2:]
    time = s[:-2]
    
    if amOrPm == 'AM':
        timeParts = time.split(":")
        if timeParts[0] == '12':
            hour = '00'
            newTime = str(hour)+":"+str(timeParts[1])+":"+str(timeParts[2])
            print(newTime)
            return(newTime)
        print(time)
        return(time)
    
    if amOrPm == "PM":
        timeParts = time.split(":")
        if timeParts[0] == '12':
            print(time)
            return(time)
        print(timeParts)
        hour = int(timeParts[0])+12
        if hour == 24:
            hour = str('00')
        newTime = str(hour)+":"+str(timeParts[1])+":"+str(timeParts[2])
        print(newTime)
        return(newTime)
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

