## High Level Requirements
|ID|Feature|Status|
|---|---|---|
HR01 |Output file generated across different computers (windows + linux)|
HR02 |Login credentials (Modify/View) |
HR03 |Input Files Based on Different Initiatives and Timelines |
HR04 |Master Calender |
HR05 |Faculty calender |
HR06 |Faculty load sheet |
HR07 | Showing Available Open Slots based on faculty and modules



HR06 |Segregation based on initiatives and months|
HR07 |Color codes for initiatives followed|
HR08 |Append the Current Output to the Previous Output|
HR09 |Error correction|
HR10 |Insights and notifications| 
HR11 |Let User know that Output has been Successfully Updated |

## Low Level Requirements
|ID|Feature|High Level ID|Status|
|--|---|---|---|
LR01|Master calender month wise |HR03,HR06|
LR02|Master calender initiative wise|HR03,HR06|
LR03|Master calender appending|HR03, HR08|
LR04|Master calender course code correction|HR03,HR09|
LR05|Master calender course title correction|HR03,HR09|
LR06|Master calender dates not analysed|HR03,HR10|
LR07|Faculty calender month wise |HR04,HR06|
LR08|Faculty calender initiative wise|HR04,HR06|
LR09|Faculty calender appending|HR04,HR08|
LR10|Faaculty name correction/validation in faculty calender|HR04,HR09|
LR11|Faculty calender conflicts (Red highlight + pop-up) |HR04,HR10|
LR12|Faculty load table month wise |HR05,HR06|
LR13|Faculty load table initiative wise|HR05,HR06|
LR14|Faculty name correction/validation in faculty load sheet|HR05,HR09|
LR15|Faculty load insight : OVERLOAD, UNDERLOAD, OPTIMUM |HR05,HR10|
LR16|Available free slots for faculty from faculty load sheet|HR05, HR10|


## Features Checklist

Feature| V0 Python Implementation | V0 Matlab Implementation|
|---|---|---|
Select file from user| Implemented | Implemented |
Provide Dropdown List for user to select Month and Initiative | Not Available | Implemented |
Output file generated across different computer| Implemented |Works only with MATLAB |
Excel file generated for one month | Implemented | Implemented |
Validates days in month in input file| Not Available|
Let User Know that the Output File has been Updated Successfully | Not Available |Implemented |
Let User Know if the rows are not Analyzed | Not Available | Implemented |
Color Coding for blocking schedule | Implemented | |









