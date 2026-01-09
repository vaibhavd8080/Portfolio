# ===========================================
# Project: Student Performance Analyzer
# Created by: Vaibhav Deshmukh
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

def analyze_results():
    print("--- System Initialization ---")
    print("Loading student records...")

    # 1. Dataset (Simulating CSV data for now)
    # Note: Using dictionary format before converting to DataFrame
    data = {
        'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
        'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Vikram', 'Anjali', 'Rohan', 'Kavita'],
        'Maths': [85, 45, 92, 35, 78, 88, 40, 95],
        'Science': [90, 55, 88, 40, 75, 92, 42, 98],
        'English': [88, 60, 91, 45, 80, 85, 44, 96]
    }

    df = pd.DataFrame(data)

    # 2. Processing Data
    # Adding total marks column
    df['Total'] = df['Maths'] + df['Science'] + df['English']
    
    # Calculating percentage - rounded to 2 decimal places
    df['Percentage'] = round(df['Total'] / 3, 2)

    # Logic: Students need at least 40% to pass the semester
    df['Status'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

    print("\n[INFO] Data processing complete. Printing Result Table:")
    print("-" * 50)
    print(df[['Name', 'Total', 'Percentage', 'Status']])
    print("-" * 50)

    # 3. Statistical Analysis
    class_avg = df['Percentage'].mean()
    
    # Finding the row with the maximum percentage
    topper_idx = df['Percentage'].idxmax()
    topper_name = df.loc[topper_idx, 'Name']
    topper_score = df.loc[topper_idx, 'Percentage']
    
    print(f"\n>> CLASS SUMMARY <<")
    print(f"Average Class Performance: {class_avg:.2f}%")
    print(f"Top Performer of the batch: {topper_name} ({topper_score}%)")

    # 4. Data Visualization
    print("\nPreparing Bar Chart...")
    
    subjects = ['Maths', 'Science', 'English']
    subject_avgs = [df['Maths'].mean(), df['Science'].mean(), df['English'].mean()]

    # Setting up the plot
    plt.figure(figsize=(10, 6))
    plt.bar(subjects, subject_avgs, color=['skyblue', 'salmon', 'lightgreen'])
    
    plt.title('Average Performance per Subject')
    plt.xlabel('Subjects')
    plt.ylabel('Average Marks')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()
    print("Process Finished Successfully.")

# Standard Python entry point
if __name__ == "__main__":
    analyze_results()
