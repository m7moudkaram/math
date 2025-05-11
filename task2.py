
import pandas as pd

# Create sample dataset
data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia', 'Kevin', 'Laura'],
    'Gender': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Age': [18, 17, 18, 19, 17, 18, 19, 18, 17, 19, 18, 18],
    'Math': [85, 92, 78, 90, 88, 76, 95, 89, 80, 93, 87, 91],
    'Science': [90, 88, 82, 85, 93, 77, 91, 84, 79, 92, 86, 89],
    'English': [88, 85, 80, 92, 87, 81, 88, 90, 83, 86, 84, 94]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Show full dataset
print("Sample Dataset:\n")
print(df)


# Step 2: Mean and median of numeric columns
numeric_cols = ['Math', 'Science', 'English']

print("\nMean Scores:")
print(df[numeric_cols].mean())

print("\nMedian Scores:")
print(df[numeric_cols].median())


# Step 3: Filter students with Math > 90
high_math = df[df['Math'] > 90]
print("\nStudents with Math > 90:")
print(high_math[['Name', 'Math']])


# Step 4: Group by Gender and get average scores
grouped = df.groupby('Gender')[numeric_cols].mean()
print("\nAverage scores by Gender:")
print(grouped)


# Step 5: Add new columns using apply and lambda
df['Average'] = df[numeric_cols].apply(lambda x: x.mean(), axis=1)

def letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    else: return 'D'

df['Grade'] = df['Average'].apply(letter_grade)

# Show final results
print("\nFinal Grades:")
print(df[['Name', 'Math', 'Science', 'English', 'Average', 'Grade']])