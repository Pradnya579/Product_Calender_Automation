
# importing the dependencies

from string import ascii_uppercase
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment, Border, Side
import numpy as np
from pandas.core.frame import DataFrame

#Taking data from GUI
Initiative = "GENESIS"
OutMonth = "July"


# Extracting data from the input calender which is in the day wise format
InputDataframe = pd.read_excel(r"C:\Users\vv972\OneDrive\Documents\MATLAB\Excel case study\Excel_Automation_Test\Automation_Sample Calender_v0.6.xlsx", sheet_name='Sample_GENESIS')
InputDataframe.columns = ['Month', 'Date', 'Day', 'Course Code', 'Module','Lead1', 'Lead2', 'Lead3', 'Session Slot', 'Session Time','Comments']
InputDataframe = InputDataframe.drop([0, 1])
InputDataframe.reset_index(inplace = True, drop= True)
#print(InputDataframe)
Date = InputDataframe['Date']
Month = InputDataframe['Month']
Day = InputDataframe['Day']
CourseCode = InputDataframe['Course Code']
Module = InputDataframe['Module']
Lead1 = InputDataframe['Lead1']
Lead2 = InputDataframe['Lead2']
Lead3 = InputDataframe['Lead3']
SessionSlot = InputDataframe['Session Slot']
Comments = InputDataframe['Comments']


# Extracting data from the Keys sheet of the Master calendar
KeysDataframe = pd.read_excel(r"C:\Users\vv972\OneDrive\Documents\MATLAB\Calender auomation product\Product_Calender_Automation\V1\Implementation\MasterCalendar/Master.xlsx", sheet_name='Key')
KeysDataframe.columns = ["FixedInitiativeTitles", "FixedInitiativeCodes", "FixedInitiativeColourCodes", "VarName4", "VarName5", "VarName6", "FixedCourseCodes", "FixedCourseTitles"]
KeysDataframe = KeysDataframe.drop(["VarName4", "VarName5", "VarName6"], axis=1)
#print(KeysDataframe)
FixedInitiativeTitles = KeysDataframe['FixedInitiativeTitles']
FixedInitiativeCodes = KeysDataframe['FixedInitiativeCodes']
FixedInitiativeColourCodes = KeysDataframe['FixedInitiativeColourCodes']                                             # reads empty data
FixedCourseCodes = KeysDataframe['FixedCourseCodes']
FixedCourseTitles = KeysDataframe['FixedCourseTitles']
FixedCourses = [FixedCourseCodes,FixedCourseTitles]
FixedCourses = pd.concat([FixedCourseCodes, FixedCourseTitles], axis = 1)                                            # Fixed Courses dataframe

#print(FixedCourses)
#print(CourseCode)
# print(Date, Day, CourseCode, Module, SessionSlot, Lead1, Lead2, Lead3)
# print(FixedInitiativeTitles, FixedInitiativeCodes, FixedCourseCodes, FixedCourseTitles)
# TO DO fix errors
# ExistingDataframe = pd.read_excel('/Users/achu/Downloads/Calendar/Master.xlsx', sheet_name=OutMonth)
# ExistingDataframe = ExistingDataframe.drop([0,1])
# ExistingDataframe.index = ExistingDataframe.index -1
# UniqueCourseCode = ExistingDataframe.iloc[:,0]
# RespectiveCourseTitleOutMonth = ExistingDataframe.iloc[:,1]
# RespectiveFacultyOutMonth = ExistingDataframe.iloc[:2:6]
# TimeTableOutMonth = ExistingDataframe.iloc[:,7:68]
# print(UniqueCourseCode, RespectiveCourseTitleOutMonth, RespectiveFacultyOutMonth ,TimeTableOutMonth)
#print(CourseCode)
#print(CourseCode[1])
#print(FixedCourseCodes)
#print(FixedCourses.iloc[1,0])


#print(CourseCode)
#print(Module)

"""Error correction :
if course code incorrect , course title correct         =   corrects course code
if course code correct   , course title  incorrect      =   corrects course title
if course code incorrect , course title also incorrect  =   replaces the course code with ""
"""

"""Fixing the error course codes"""
for i in range(0, len(CourseCode)):
    TempFlag=0
    for j in range(0, len(FixedCourseCodes)):
        if (CourseCode[i] == FixedCourseCodes[j]):
            TempFlag = 1
    if TempFlag == 0:
        TempFlagError = 1
        for k in range(0, len(FixedCourseTitles)):
            if (Module[i] == FixedCourseTitles[k]):
                CourseCode[i] = FixedCourseCodes[k]
                TempFlagError = 0
        if TempFlagError == 1:
            CourseCode[i] = ""
#print(CourseCode)
#print(Module)

"Fixing the error course titles"
for i in range(0, len(Module)):
    TempFlag=0
    for j in range(0, len(FixedCourseTitles)):
        if (Module[i] == FixedCourseTitles[j]):
            TempFlag = 1
    if TempFlag == 0:
        TempFlagError = 1
        for k in range(0, len(FixedCourseCodes)):
            if (CourseCode[i] == FixedCourseCodes[k]):
                Module[i] = FixedCourseTitles[k]
                TempFlagError = 0
        if TempFlagError == 1:
            CourseCode[i] = ""

#print(CourseCode)
#print(Module)

"""Selecting the particular initaitive code"""
InitiativeCode = 11
for i in range(0, len(FixedInitiativeTitles)):
    if Initiative == FixedInitiativeTitles[i]:
        InitiativeCode = FixedInitiativeCodes[i]
#print(InitiativeCode)



"""UniqueCourseCode containing unique data for CourseCode"""
UniqueCourseCode = []
for i in range(0, len(CourseCode)):
    if CourseCode[i] != '' and CourseCode[i] not in UniqueCourseCode:
        UniqueCourseCode.append(CourseCode[i])
UniqueCourseCode=pd.Series(UniqueCourseCode)
#print(UniqueCourseCode)




"""Declaring variable to hold respective CourseTitle for UniqueCourseCode"""
RespectiveCourseTitle = pd.Series([""]*len(UniqueCourseCode))
#print(RespectiveCourseTitle)


"""Declaring matrix to hold repeatitive list of faculties for respective UniqueCourseCode"""
Faculty =pd.DataFrame([[""]*len(CourseCode)*3]*len(UniqueCourseCode))
#print(Faculty)