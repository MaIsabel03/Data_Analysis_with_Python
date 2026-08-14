# **Grade Estimator (Final Project Units 1–8)**

This project is a Python program developed step by step through Units 1–8. It calculates the estimated course grade using scores from discussions, course projects, and core assessments. The program reads data from external files instead of hardcoding values, so it automatically updates if the grades or assignment rules change.

## **What the Program Does**

- **Unit 1 →** Asks for your first and last name, cleans it up, and prints a greeting.
- **Units 2–4 →** In earlier units, grades were hardcoded, but now all grades come from files (JSON and CSV).
- **Unit 5 →** Reads tasks.json to know how many assignments there are and their maximum points.
- **Unit 6 →** Connects to the World Time API to show the current date, time, and how many weeks of the class have passed.
- **Unit 7 →** Loads grades.csv and cleans the grades (removes negatives, caps scores at maximum, keeps blanks).
- **Unit 8 →** Reads grades_0.csv or grades_50.csv, calculates total points, maximum points, percentage, and a letter grade (A–F).

## **Features**

- Greets the user with their name (formatted Last, First).  
- Reads assignment rules from `tasks.json`.  
- Loads grades from external CSV files instead of hardcoding.  
- Cleans grades (removes negatives, caps scores, keeps blanks).  
- Connects to the World Time API to show current date, time, client IP, and class progress.  
- Calculates averages, total points, percentage, and final letter grade (A–F).  
- Supports multiple grade scenarios (`grades_0.csv` vs. `grades_50.csv`). 

## **Files Needed**

The program depends on four external files:

1. `tasks.json` → Defines assignment types and rules (number of tasks, max points each)  
2. `grades.csv` → Original grades for all units  
3. `grades_0.csv` → Copy of `grades.csv` with Unit 8 grades set to 0 (shows what happens if Unit 8 is not done)  
4. `grades_50.csv` → Copy of `grades.csv` with Unit 8 grades set to 50 (shows what happens if Unit 8 is done with full credit)  

## **How to Run It**

1. Make sure you have **Python 3** installed.
2. Install the required libraries: `bash pip install pandas requests`
3. Run the program: `python GradeEstimator_ID.py`
4. Follow the prompts and program steps:
- Enter your first name and last name.
- The program will greet you (last name first, then first name).
- It shows the maximum grade possible for the class.
- It displays information from the World Time API (client IP, day of year, UTC datetime, and number of weeks completed).
- It prints out the original grades data, then the discussion grades and Unit 1 grades.
- It shows the cleaned grades data (negative values fixed, scores capped, blanks preserved).
- You will be asked which file to load: `grades_0.csv` (if Unit 8 is not done) or `grades_50.csv` (if Unit 8 is done with full credit).
- Finally, it calculates and prints your total points, maximum points, percentage, and letter grade.

### **Example Outputs**
```
Enter your first name: marcela
Enter your last name: redondo
Hello Redondo, Marcela
Maximum grade you can get for this class is: 1000
Client IP: XXX.XX.XXX.XXX
Day of Year: 275
UTC Datetime: 2025-10-03T00:43:11.103257+00:00
You have completed 8 weeks of 8

=== Original Grades Data ===
               type  week1  week2  week3  week4  week5  week6  week7  week8
0       discussions     50   50.0     50  -50.0     50   50.0     50   50.0
1   course_projects     50   50.0     50   50.0     85   50.0     50   50.0
2  core_assessments     50    NaN     50    NaN     50    NaN     50    NaN

=== Cleaned Grades Data ===
               type  week1  week2  week3  week4  week5  week6  week7  week8
0       discussions     50     50     50      0     50     50     50     50
1   course_projects     50     50     50     50     50     50     50     50
2  core_assessments     50   <NA>     50   <NA>     50   <NA>     50   <NA>

Enter which file to load (grades_0.csv or grades_50.csv): grades_50.csv
``` 

**If Unit 8 is not done (`grades_0.csv`):**

```
=== FINAL GRADE REPORT ===
You have 900 out of 1000
Your percentage is 90.00%
Your letter grade is: B
```

**If Unit 8 is done with full credit (`grades_50.csv`):**

```
=== FINAL GRADE REPORT ===
You have 1000 out of 1000
Your percentage is 100.00%
Your letter grade is: A
```

## **Repository Contents**

1. `GradeEstimator_ID.py` →** main Python file (all units combined)
2. `tasks.json` →** assignment rules
3. `grades.csv` →** original grades
4. `grades_0.csv` →** Unit 8 grades set to 0
5. `grades_50.csv` →** Unit 8 grades set to 50
6. `unit1/` →** screenshot(s) for Unit 1
7. `unit2/` →** screenshot(s) for Unit 2
8. `unit3/` →** screenshot(s) for Unit 3
9. `unit4/` →** screenshot(s) for Unit 4
10. `unit5/` →** screenshot(s) for Unit 5
11. `unit6/` →** screenshot(s) for Unit 6
12. `unit7/` →** screenshot(s) for Unit 7
13. `unit8/` →** screenshot(s) for Unit 8
14. `README.md` →** this document

## **Notes**

This project was built step by step as part of the CIS615: Data analysis with Python course.
It covers:
- Taking input and showing output
- Using JSON and CSV files
- Connecting to APIs
- Calculating total points, percentages, and letter grades

The project is kept simple to make it easy to follow.
