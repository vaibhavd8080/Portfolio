import pandas as pd
import matplotlib.pyplot as plt

# --- Student Result Analysis System ---
# Project by: Vaibhav Deshmukh
# Goal: To analyze class performance and find the topper

def analyze_results():
    print("--- Starting Result Analysis ---")

    # 1. Simulating Data (In real life, this would load from a CSV file)
    data = {
        'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
        'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Vikram', 'Anjali', 'Rohan', 'Kavita'],
        'Maths': [85, 45, 92, 35, 78, 88, 40, 95],
        'Science': [90, 55, 88, 40, 75, 92, 42, 98],
        'English': [88, 60, 91, 45, 80, 85, 44, 96]
    }

    df = pd.DataFrame(data)

    # 2. Data Cleaning & Calculation
    # Calculate Total and Percentage for each student
    df['Total'] = df['Maths'] + df['Science'] + df['English']
    df['Percentage'] = round(df['Total'] / 3, 2)

    # Determine Pass/Fail (Pass if Percentage >= 40)
    # Using a simple lambda function for logic
    df['Status'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

    print("\n--- Class Result Sheet ---")
    print(df[['Name', 'Total', 'Percentage', 'Status']])

    # 3. Finding Insights (Data Analyst Logic)
    avg_class_score = df['Percentage'].mean()
    topper = df.loc[df['Percentage'].idxmax()]
    
    print("\n--- Key Insights ---")
    print(f"Class Average: {avg_class_score:.2f}%")
    print(f"Class Topper: {topper['Name']} with {topper['Percentage']}%")

    # 4. Visualization
    # Showing a comparison of Subject Averages
    subjects = ['Maths', 'Science', 'English']
    averages = [df['Maths'].mean(), df['Science'].mean(), df['English'].mean()]

    print("\nGenerating Graph...")
    plt.bar(subjects, averages, color=['orange', 'green', 'blue'])
    plt.title('Average Marks per Subject')
    plt.ylabel('Marks')
    plt.show()

if _name_ == "_main_":
    analyze_results()
