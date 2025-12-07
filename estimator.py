"""
Project: Smart Construction Material Estimator
Author: Vaibhav Deshmukh
Description: A Python tool to automate material estimation for Civil Engineering.
             It calculates brick requirements based on wall dimensions and 
             logs the cost estimates to a CSV file for data analysis.
Tech Stack: Python, CSV. Module
"""

import csv
import os

def calculate_bricks(length, height, thickness):
    """
    Calculates the number of bricks required for a wall.
    """
    # Standard metric brick size in meters (0.2m x 0.1m x 0.1m with mortar)
    brick_volume = 0.2 * 0.1 * 0.1 
    
    wall_volume = length * height * thickness
    
    total_bricks = wall_volume / brick_volume
    
    # Adding 5% buffer for material wastage/breakage
    total_bricks = total_bricks * 1.05
    
    return int(total_bricks)

def save_to_file(project_name, bricks):
    """
    Saves the estimation data to a CSV file. 
    Checks if file exists to avoid overwriting or duplicating headers.
    """
    filename = 'construction_data.csv'
    file_exists = os.path.isfile(filename)
    
    # 'a' mode appends data to the end of the file without deleting history
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers only if the file is being created for the first time
        if not file_exists:
            writer.writerow(["Project Name", "Total Bricks Needed", "Estimated Cost (Rs)"])
        
        # Assuming current market rate: 8 Rs per brick
        cost = bricks * 8
        writer.writerow([project_name, bricks, cost])
        print(f"\n[SUCCESS] Data saved to {filename}. Estimated Cost: Rs {cost}")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Civil Engineer's Material Estimator ---")
    
    try:
        p_name = input("Enter Site/Project Name: ")
        l = float(input("Enter Wall Length (m): "))
        h = float(input("Enter Wall Height (m): "))
        t = float(input("Enter Wall Thickness (m): "))

        if l < 0 or h < 0 or t < 0:
            print("Error: Dimensions cannot be negative.")
        else:
            bricks_needed = calculate_bricks(l, h, t)
            print(f"\nResult: You need approximately {bricks_needed} bricks.")
            save_to_file(p_name, bricks_needed)

    except ValueError:
        print("\n[Error] Invalid Input: Please enter numeric values for dimensions.")
