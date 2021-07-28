## High Level Requirements
|ID|Feature| MATLAB v0 Status| Python v0 Status |
|---|---|---|----|
HR01 |Output file generated across different computers (windows + linux)| Not Available | |
HR02 |Login credentials (Modify/View) | Not Available | |
HR03 |Input Files Based on Different Initiatives and Timelines | Implemented | |
HR04 |Master Calender | Implemented | |
HR05 |Faculty calender | Implemented | |
HR06 |Faculty load sheet | Implemented | |
HR07 |Showing Available Open Slots based on faculty and modules | Not Available | | 


## Low Level Requirements
|ID|Feature|High Level ID| MATLAB v0 Status| Python v0 Status |
|--|---|---|---|----|
LR01|Master Calendar display month wise |HR04| Implemented | Implemented|
LR02|Master Calendar display initiative wise|HR04| Implemented | |
LR04|Master Calendar Differentiate Initiatives (Color Codes/Numbers)|HR04| Implemented | Implemented|
LR05|Master Calendar Appending|HR04| Implemented | | 
LR06|Master Calendar Course code correction|HR04| Implemented | |
LR07|Master Calendar Course title correction|HR04| Not Available | |
LR08|Master Calendea display the dates that were not analysed|HR04| Implemented | |
LR09|Faculty Calendar display Month wise |HR05| Implemented | |
LR010|Faculty Calendar display Initiative wise|HR05| Implemented | |
LR011|Faculty Calendar Appending|HR05| Implemented | |
LR012|Faculty Calendar: Differentiate Initiatives (Color Codes/Numbers)|HR05| Implemented |Implemented |
LR13|Faculty name correction/validation in faculty calender|HR05| Not Available | |
LR14|Faculty Calendar: Highlight conflicts (Red highlight/pop-up/Concatenated Numbers) |HR05| Implemented | |
LR15|Faculty Load Sheet display Month wise |HR06|Implemented | |
LR16|Faculty Load Sheet display Initiative wise|HR06|Implemented | |
LR17|Faculty name correction/validation in Faculty Load Sheet|HR06| Not Available | |
LR18|Faculty Load Sheet: Display Available Slots Faculty wise|HR06| Not Available | | 
LR18|Faculty load insight : OVERLOAD, UNDERLOAD, OPTIMUM |HR06| Not Available | |
LR19|Faculty Load Sheet Appending|HR06| Implemented | |
LR20|Available free slots for faculty from faculty load sheet|HR07| Not Available | |
LR21 |Let User know that the Output has been Successfully Updated |HR05,HR06,HR07|Implemented | |
LR22|Master calender check no entry datas whether weekend/missing|HR04||
LR23|Validate correct number of days in month|HR04,HR05||



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









