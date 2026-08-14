# **Grade Estimator -- Data Analysis with Python Class**

The Grade Estimator is a Python-based data processing and analysis project developed as the final project for CIS615: Data Analysis with Python. The program processes course assignment data from external JSON and CSV files, validates and cleans grade data, integrates with the World Time API, and calculates total points, percentages, and final letter grades.

The project was developed incrementally across Units 1–8, with each unit adding new functionality and building toward the final program.

## **What the Program Does?**

The program automates the process of estimating a student's course grade by using assignment rules and grade data stored in external files rather than relying on hardcoded values.

This approach allows the program to:

- Process changing grade data without modifying the core program
- Apply consistent rules to incomplete or invalid grade values
- Calculate total and maximum available points
- Compare different grade scenarios
- Generate a final percentage and letter grade
- Provide information about course progress

## **Key Features** 

- Data processing with Python and Pandas
- Reads assignment rules from a JSON file
- Loads grade data from CSV files
- Cleans and validates grade values
- Removes negative scores and caps scores at their maximum allowed value
- Preserves blank values for incomplete assessments
- Calculates total points and maximum possible points
- Calculates overall percentage and letter grade
- Supports multiple grade scenarios
- Integrates with the World Time API
- Calculates course progress based on elapsed weeks
- Uses external data sources instead of hardcoding assignment and grade information

## **Files Needed**

The program depends on four external files:

1. `tasks.json` → Defines assignment types and rules (number of tasks, max points each)  
2. `grades.csv` → Original grades for all units  
3. `grades_0.csv` → Copy of `grades.csv` with Unit 8 grades set to 0 (shows what happens if Unit 8 is not done)  
4. `grades_50.csv` → Copy of `grades.csv` with Unit 8 grades set to 50 (shows what happens if Unit 8 is done with full credit)

## **Programs & Tools Used**

### **Languages & Libraries**
- Python
- Pandas
- Requests
### **Data & File Handling** 
- CSV
- JSON
- Data cleaning
- Data validation
- Data processing
### **Other** 
- REST API integration
- Business-rule-based calculations
- Scenario analysis
- Automated reporting

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

## **Repository Structure**

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

## **Project Context**

This project was completed as part of CIS615: Data Analysis with Python and developed incrementally across Units 1–8. 

The project demonstrates practical experience with data processing, validation, external data sources, API integration, calculations, and presenting analytical results through a Python application.

## **Portfolio Relevance**

This project demonstrates skills applicable to Data Analyst and Business Analyst roles, particularly in:

- Working with structured data
- Identifying and handling data-quality issues
- Applying business rules to data
- Automating repetitive calculations
- Working with external data sources
- Comparing scenarios and outcomes
- Translating raw data into meaningful results
