from string import ascii_uppercase
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment, Border, Side

#Taking data from GUI
Initiative = "GENESIS"
OutMonth = "July"
# Reading input from May_Calendar
InputDataframe = pd.read_excel('C:\Users\vv972\OneDrive\Documents\MATLAB\Calender auomation product\Product_Calender_Automation\V1\Calender_Automation_Test\Additional Calenders\GENESIS\May_Calendar_v0.1.xlsx', sheet_name='Test vector')
InputDataframe.columns = ['Month', 'Date', 'Day', 'Course Code', 'Module',
                             'Lead1', 'Lead2', 'Lead3', 'Session Slot', 'Session Time','Comments']
InputDataframe = InputDataframe.drop([0, 1])
Date = InputDataframe['Date']
Date = Date.dropna()
Date.index = Date.index - 1
Month = InputDataframe['Month']
Month = set(Month.dropna())
Day = InputDataframe['Day']
Day = Day.dropna()
Day.index = Day.index - 1
CourseCode = InputDataframe['Course Code']
CourseCode.index = CourseCode.index - 1
Module = InputDataframe['Module']
Module.index = Module.index - 1
Lead1 = InputDataframe['Lead1']
Lead1.index = Lead1.index - 1
Lead2 = InputDataframe['Lead2']
Lead2.index = Lead2.index - 1
Lead3 = InputDataframe['Lead3']
Lead3.index = Lead3.index - 1
SessionSlot = InputDataframe['Session Slot']
SessionSlot.index = SessionSlot.index - 1
Comments = InputDataframe['Comments']
Comments.index = Comments.index - 1
# Reading Keys from Master calendar
KeysDataframe = pd.read_excel('C:\Users\vv972\OneDrive\Documents\MATLAB\Calender auomation product\Product_Calender_Automation\V1\Implementation\MasterCalendar/Master.xlsx', sheet_name='Key')
KeysDataframe.columns = ["FixedInitiativeTitles", "FixedInitiativeCodes", "FixedInitiativeColourCodes", "VarName4", "VarName5", "VarName6", "FixedCourseCodes", "FixedCourseTitles"]
KeysDataframe = KeysDataframe.drop(["VarName4", "VarName5", "VarName6"], axis=1)
FixedInitiativeTitles = KeysDataframe['FixedInitiativeTitles']
FixedInitiativeTitles = FixedInitiativeTitles.dropna()
FixedInitiativeTitles.index = FixedInitiativeTitles.index + 1
FixedInitiativeCodes = KeysDataframe['FixedInitiativeCodes']
FixedInitiativeCodes = FixedInitiativeCodes.dropna()
FixedInitiativeCodes.index = FixedInitiativeCodes.index + 1
FixedInitiativeColourCodes = KeysDataframe['FixedInitiativeColourCodes']  ## reads empty data
FixedCourseCodes = KeysDataframe['FixedCourseCodes']
FixedCourseCodes = FixedCourseCodes.dropna()
FixedCourseCodes.index = FixedCourseCodes.index + 1
FixedCourseTitles = KeysDataframe['FixedCourseTitles']
FixedCourseTitles = FixedCourseTitles.dropna()
FixedCourseTitles.index = FixedCourseTitles.index + 1
# Fixed Courses dataframe
FixedCourses = [FixedCourseCodes, FixedCourseTitles]
FixedCourses = pd.concat([FixedCourseCodes, FixedCourseTitles], axis = 1)

# print(FixedCourses)
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





