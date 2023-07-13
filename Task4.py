# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 05:29:02 2023

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
    
    return nod
    
def dayOfYear(year, month, day):
    month_lst = ["January", "February","March", "April", "May", "June",
                 "July","August","September","October","November", "December"] 
    
    sum_days = 0
    
    for imonth in month_lst:
        if imonth == month:
            break
        else:
            sum_days += daysInMonth(year, imonth)
    result = day + sum_days
    return result 

print(dayOfYear(2000, "December", 31))

