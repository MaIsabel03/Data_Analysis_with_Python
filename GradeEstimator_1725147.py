# ----------- UNIT 1 REQUIREMENTS -----------

# Ask the user for their first name
first_name = input("Enter your first name: ")

# Ask the user for their last name
last_name = input("Enter your last name: ")

# Remove extra spaces and capitalize the first letter of the first name
first_name = first_name.strip().capitalize()

# Remove extra spaces and capitalize the first letter of the last name
last_name = last_name.strip().capitalize()

# Print a greeting message with last name first, then first name
print(f"Hello {last_name}, {first_name}")

# ----------- NOTE ABOUT UNIT 2–4 -----------
# Units 2–4 originally contained hardcoded grade variables (e.g., Unit1_discussion_points = 50).
# For Unit 8, the assignment requires that all task properties and grades
# come from external files (tasks.json and grades_0.csv/grades_50.csv).
# This makes the program flexible: changing grades in CSV or rubric in JSON
# will automatically update the calculations without changing the Python code.
# Therefore, all the old Unit 2–4 sections were removed.

# ----------- UNIT 5 REQUIREMENTS -----------

import json  # Import json library so we can read data from tasks.json

# Define a class to represent a type of task (discussion, course project, core assessment)
class Task_type:
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):
        # Save the name of the task type (e.g., "discussions")
        self.name = name
        # Save the display name (e.g., "Discussions")
        self.display_name = display_name
        # Save how many tasks of this type exist in the semester (e.g., 8 discussions)
        self.tasks_per_semester = tasks_per_semester
        # Save the maximum points per task (e.g., 50 points each)
        self.maximum_points_per_task = maximum_points_per_task

# Open and read the tasks.json file which defines the tasks and their properties
with open("tasks.json", "r") as file:
    tasks_data = json.load(file)  # Load JSON data into Python as a list of dictionaries

# Create an empty list to store Task_type objects
task_types = []

# Loop over each task definition from JSON and create Task_type objects
for task in tasks_data:
    task_obj = Task_type(
        task["name"],                 # Internal name (e.g., "discussions")
        task["display_name"],         # Human-readable name (e.g., "Discussions")
        task["tasks_per_semester"],   # How many times this task occurs (e.g., 8)
        task["maximum_points_per_task"]  # Max score for each task (e.g., 50)
    )
    # Add the created object to our list
    task_types.append(task_obj)

# Calculate the maximum possible points in the course by summing over all task types
total_max_points = sum(t.tasks_per_semester * t.maximum_points_per_task for t in task_types)

# Display the maximum grade possible in the course
print(f"Maximum grade you can get for this class is: {total_max_points}")

# ----------- UNIT 6 REQUIREMENTS -----------

import requests  # Import requests library to fetch data from an online API
from datetime import datetime  # Import datetime to handle dates and times

# Get the current time and date data from the World Time API for Chicago timezone
response = requests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
data = response.json()  # Convert the response into a Python dictionary

# Extract the client IP address from the API response
client_ip = data["client_ip"]

# Extract the day of year from the API response (1–365/366)
day_of_year = data["day_of_year"]

# Extract the UTC datetime string from the API response
utc_datetime = data["utc_datetime"]

# Print the extracted information
print("Client IP:", client_ip)
print("Day of Year:", day_of_year)
print("UTC Datetime:", utc_datetime)

# Define the day of year when the course begins (August 11, 2025)
begin_course_day = datetime(2025, 8, 11).timetuple().tm_yday

# Convert the unix timestamp from the API response into a datetime object
now_date = datetime.fromtimestamp(data["unixtime"])

# Get the day of year for the current date
now_day = now_date.timetuple().tm_yday

# Calculate how many days have passed since the course started
days_passed = now_day - begin_course_day

# Convert days into weeks (7 days = 1 week/unit)
weeks_completed = days_passed // 7 + 1

# Cap the number of units to 8 maximum (since the course has 8 units)
if weeks_completed > 8:
    weeks_completed = 8

# Print the number of completed weeks/units
print(f"You have completed {weeks_completed} weeks of 8")

# ----------- UNIT 7 REQUIREMENTS -----------

import pandas as pd  # Import pandas library to work with CSV data

# Load the original grades.csv file into a DataFrame
grades = pd.read_csv("grades.csv")

# Display the full DataFrame (all original grades from CSV)
print("\n=== Original Grades Data ===")
print(grades)

# Display only the rows where the type is "discussions"
print("\n=== Discussion Grades ===")
print(grades[grades["type"] == "discussions"])

# Display the grades for Unit 1 (week1) across all task types
print("\n=== Grades for Unit 1 (Week 1) ===")
print(grades[["type", "week1"]])

# Reload maximum grade value from JSON file (avoid hardcoding max points)
with open("tasks.json", "r") as file:
    tasks_data = json.load(file)

# Get the maximum grade per task from JSON
max_grade = max(task["maximum_points_per_task"] for task in tasks_data)

# Define a function to clean grade values (handle blanks, negatives, and values above max)
def clean_grade(value):
    if pd.isna(value):  # If value is NaN (blank), keep it blank
        return value
    value = int(value)  # Convert the grade to an integer
    if value < 0:       # Negative values are not allowed, set to 0
        return 0
    elif value > max_grade:  # If value exceeds max grade, cap it at max
        return max_grade
    else:
        return value  # Otherwise keep the grade as is

# Make a copy of the grades DataFrame to clean
cleaned_grades = grades.copy()

# Apply cleaning to all week columns (skip the "type" column)
for col in cleaned_grades.columns[1:]:
    cleaned_grades[col] = cleaned_grades[col].apply(clean_grade)

# Convert numeric columns to integers, but allow blanks (Int64 type supports NaN)
cleaned_grades = cleaned_grades.astype({col: "Int64" for col in cleaned_grades.columns if col != "type"})

# Display cleaned grade data
print("\n=== Cleaned Grades Data ===")
print(cleaned_grades)

# ----------- UNIT 8 REQUIREMENTS -----------

# Ask the user which CSV file to load (grades_0.csv or grades_50.csv)
filename = input("Enter which file to load (grades_0.csv or grades_50.csv): ")

# Load the chosen grades file into a DataFrame
grades = pd.read_csv(filename)

# Load task properties again from tasks.json
with open("tasks.json", "r") as file:
    tasks_data = json.load(file)

# Initialize earned and maximum points to zero
earned_points = 0
max_points = 0

# Loop through each row in the CSV (discussions, course_projects, core_assessments)
for _, row in grades.iterrows():
    task_name = row["type"]  # Get the type (matches JSON names)

    # Find task details in the JSON file
    task_info = next((t for t in tasks_data if t["name"] == task_name), None)
    if not task_info:  # Skip if not found
        continue

    max_task_points = task_info["maximum_points_per_task"]  # e.g., 50
    tasks_allowed = task_info["tasks_per_semester"]         # e.g., 8 or 4

    week_columns = [col for col in row.index if col.startswith("week")]  # Collect week columns

    counted = 0  # Counter to ensure we only count the allowed number of tasks
    for week in week_columns:
        if counted >= tasks_allowed:  # Stop if we've reached allowed tasks
            break

        grade_val = row[week]  # Get the grade for that week
        if pd.isna(grade_val) or grade_val == "":  # Skip blanks
            continue
        else:
            grade_val = int(grade_val)  # Convert to integer

        earned_points += grade_val     # Add to earned total
        max_points += max_task_points  # Add to possible maximum
        counted += 1                   # Increase counter of counted tasks

# Print final results
print("\n=== FINAL GRADE REPORT ===")
print(f"You have {earned_points} out of {max_points}")  # Show raw points
percentage = (earned_points / max_points) * 100 if max_points > 0 else 0  # Compute percentage
print(f"Your percentage is {percentage:.2f}%")  # Show percentage

# Determine letter grade based on percentage
if percentage > 90:
    letter = "A"
elif percentage > 80:
    letter = "B"
elif percentage > 70:
    letter = "C"
elif percentage > 60:
    letter = "D"
else:
    letter = "F"

# Print the letter grade
print(f"Your letter grade is: {letter}")
