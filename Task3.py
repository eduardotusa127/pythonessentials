# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:41:43 2023

@author: Eduardo Tusa
"""
def isYearLeap(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False

def daysInMonth(year, month):
    month_lst = ["January", "February","March", "April", "May", "June",
                 "July","August","September","October","November", "December"] 
    
    days_lst = [31,[28,29],31,30,31,30,31,31,30,31,30,31]
    
    for i in range(len(month_lst)):
        if  month == "February": 
            if isYearLeap(year): 
                nod = days_lst[1][1]
            else:
                nod = days_lst[1][0]
        else:
            if month_lst[i] == month:
                nod = days_lst[i]
    print(nod)
    return nod
    

testYears = [1900, 2000, 2016, 1987]
testMonths = ["February", "February", "January", "November"]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
