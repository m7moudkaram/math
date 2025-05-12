import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
df = pd.read_csv('students.csv')

# Step 2: Clean Data
print("Initial Missing Values:\n", df.isnull().sum())

# Drop missing values
df.dropna(inplace=True)

# Fix data types if needed
df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
df['Study Hours'] = pd.to_numeric(df['Study Hours'], errors='coerce')
df['Attendance (%)'] = pd.to_numeric(df['Attendance (%)'], errors='coerce')
df['Exam Score'] = pd.to_numeric(df['Exam Score'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Step 3: Analyze GPA, Study Hours, Best Performing Students
avg_gpa = df['GPA'].mean()
avg_study_hours = df['Study Hours'].mean()
top_students = df.sort_values(by='Exam Score', ascending=False).head(10)

print(f"\nAverage GPA: {avg_gpa:.2f}")
print(f"Average Study Hours: {avg_study_hours:.2f}")
print("\nTop 10 Students by Exam Score:\n", top_students[['Name', 'Exam Score']])

# Step 4: Group Data by Major and Gender
gpa_by_major = df.groupby('Major')['GPA'].mean().sort_values(ascending=False)
gpa_by_gender = df.groupby('Gender')['GPA'].mean()

print("\nAverage GPA by Major:\n", gpa_by_major)
print("\nAverage GPA by Gender:\n", gpa_by_gender)

# Step 5: Calculate Performance Level (Exam Score Classification)
def classify_performance(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 75:
        return 'Good'
    elif score >= 60:
        return 'Average'
    else:
        return 'Needs Improvement'

df['Performance Level'] = df['Exam Score'].apply(classify_performance)

# Step 6: Use apply() to create new column - Study Efficiency
def study_efficiency(row):
    if row['Study Hours'] > 15 and row['Exam Score'] > 90:
        return 'Highly Efficient'
    elif row['Study Hours'] > 10 and row['Exam Score'] > 75:
        return 'Efficient'
    else:
        return 'Low Efficiency'

df['Study Efficiency'] = df.apply(study_efficiency, axis=1)

# Step 7: Visualizations

# Top 5 Majors by Average GPA (Bar Chart)
gpa_by_major.head(5).plot(kind='bar', title='Top 5 Majors by Average GPA', ylabel='GPA', figsize=(10,6))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of Performance Levels (Pie Chart)
perf_counts = df['Performance Level'].value_counts()
perf_counts.plot(kind='pie', autopct='%1.1f%%', title='Performance Level Distribution', figsize=(8,8))
plt.ylabel('')
plt.tight_layout()
plt.show()

# GPA vs Exam Score Scatter Plot
plt.figure(figsize=(10,6))
plt.scatter(df['GPA'], df['Exam Score'], alpha=0.6)
plt.title('GPA vs Exam Score')
plt.xlabel('GPA')
plt.ylabel('Exam Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 8: Summary Statistics
print("\nDescriptive Statistics:\n", df.describe())

summary = df.agg({
    'GPA': ['mean', 'max', 'min'],
    'Exam Score': ['mean', 'max', 'min']
})
print("\nCustom Aggregation:\n", summary)

print("\nPerformance Level Counts:\n", df['Performance Level'].value_counts())
print("\nStudy Efficiency Counts:\n", df['Study Efficiency'].value_counts())

# Optional: Save cleaned and enriched data
df.to_csv('cleaned_students_data.csv', index=False)