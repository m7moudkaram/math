import numpy as np
import matplotlib.pyplot as plt

# Theoretical Summary of NumPy
"""
NumPy (Numerical Python) is a fundamental package for scientific computing in Python.
It provides:
1. A powerful N-dimensional array object
2. Sophisticated broadcasting functions
3. Tools for integrating C/C++ and Fortran code
4. Linear algebra, Fourier transform, and random number capabilities

NumPy matters because:
- It provides efficient array operations that are much faster than Python lists
- It's the foundation for many other scientific Python packages (Pandas, SciPy, etc.)
- It enables vectorized operations, eliminating the need for explicit loops
- It provides a consistent interface for working with multi-dimensional data
"""

# Creating a custom dataset (100 rows × 5 columns)
# This dataset represents student performance metrics:
# - Column 1: Math scores (0-100)
# - Column 2: Science scores (0-100)
# - Column 3: English scores (0-100)
# - Column 4: Attendance percentage (0-100)
# - Column 5: Study hours per week (0-20)

# Generate random data
np.random.seed(42)  # For reproducibility
student_data = np.random.normal(loc=[75, 70, 80, 85, 10], 
                              scale=[15, 15, 15, 10, 3], 
                              size=(100, 5))

# Ensure values are within reasonable ranges
student_data = np.clip(student_data, [0, 0, 0, 0, 0], [100, 100, 100, 100, 20])

print("Dataset Shape:", student_data.shape)
print("\nFirst 5 rows of the dataset:")
print(student_data[:5])

# 1. Basic Array Operations
print("\n1. Basic Array Operations:")
print("Mean of each subject:", np.mean(student_data, axis=0))
print("Standard deviation of each subject:", np.std(student_data, axis=0))
print("Minimum values:", np.min(student_data, axis=0))
print("Maximum values:", np.max(student_data, axis=0))

# 2. Array Reshaping and Transposing
reshaped_data = student_data.reshape(20, 5, 5)
print("\n2. Reshaped array dimensions:", reshaped_data.shape)
transposed_data = student_data.T
print("Transposed array dimensions:", transposed_data.shape)

# 3. Statistical Functions
print("\n3. Statistical Analysis:")
print("Median of each subject:", np.median(student_data, axis=0))
print("25th percentile:", np.percentile(student_data, 25, axis=0))
print("75th percentile:", np.percentile(student_data, 75, axis=0))

# 4. Array Indexing and Slicing
print("\n4. Array Indexing and Slicing:")
print("Students with Math scores > 90:", student_data[student_data[:, 0] > 90])
print("Average study hours for top performers:", 
      np.mean(student_data[student_data[:, 0] > 90, 4]))

# 5. Array Operations
print("\n5. Array Operations:")
# Calculate weighted average (giving more weight to Math and Science)
weights = np.array([0.3, 0.3, 0.2, 0.1, 0.1])
weighted_avg = np.average(student_data, weights=weights, axis=1)
print("Weighted average scores for first 5 students:", weighted_avg[:5])

# 6. Array Manipulation
print("\n6. Array Manipulation:")
# Sort students by Math scores
sorted_indices = np.argsort(student_data[:, 0])
sorted_data = student_data[sorted_indices]
print("Top 5 Math scores:", sorted_data[-5:, 0])

# 7. Mathematical Functions
print("\n7. Mathematical Functions:")
print("Square root of study hours:", np.sqrt(student_data[:, 4]))
print("Exponential of attendance:", np.exp(student_data[:, 3]/100))

# 8. Array Comparison
print("\n8. Array Comparison:")
# Find students who perform well in all subjects
good_performers = np.all(student_data[:, :3] > 80, axis=1)
print("Number of students with scores > 80 in all subjects:", np.sum(good_performers))

# 9. Array Concatenation
print("\n9. Array Concatenation:")
# Add a new column for total score
total_scores = np.sum(student_data[:, :3], axis=1, keepdims=True)
student_data_with_total = np.concatenate([student_data, total_scores], axis=1)
print("Shape after adding total scores:", student_data_with_total.shape)

# 10. Array Broadcasting
print("\n10. Array Broadcasting:")
# Normalize scores to 0-1 range
normalized_scores = student_data[:, :3] / 100
print("Normalized scores (first 5 students):")
print(normalized_scores[:5])

# Visualization
plt.figure(figsize=(12, 6))
plt.boxplot(student_data[:, :3], labels=['Math', 'Science', 'English'])
plt.title('Distribution of Subject Scores')
plt.ylabel('Score')
plt.savefig('subject_scores_distribution.png')
plt.close()

print("\nA box plot has been saved as 'subject_scores_distribution.png'")