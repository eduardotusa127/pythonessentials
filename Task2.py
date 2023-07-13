# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:29:59 2023

@author: Eduardo Tusa
"""

def isYearLeap(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")

    result = isYearLeap(yr)

    if result == testResults[i]:
        print("OK") 
    else: 
        print("Failed")


