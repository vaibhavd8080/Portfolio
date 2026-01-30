# Telco Customer Churn Analysis (Power BI)

This project is based on customer churn analysis for a telecom company using Power BI. The main objective was to understand why customers are leaving the service and identify the factors that contribute most to churn.

I worked on cleaning the dataset, transforming columns in Power Query, creating DAX measures, and designing an interactive dashboard that helps explore churn patterns from different angles.

## Project Objective
- Analyze customer churn behavior
- Identify high-risk customer segments
- Understand the impact of contract type, tenure, services, and payment methods on churn
- Present insights through a clean and interactive Power BI dashboard

## Dataset Overview
The dataset contains customer-level information such as:
- Customer demographics (gender, senior citizen)
- Account details (contract type, tenure, payment method)
- Services used (internet service, phone service, add-ons)
- Monthly charges and churn status

## Data Cleaning & Preparation
The following steps were performed before building the dashboard:
- Converted churn column into binary values (0 = retained, 1 = churned)
- Removed blank and inconsistent values
- Corrected data types for numeric and categorical columns
- Standardized column names for easier analysis
- Created calculated columns and measures using DAX

## Key Insights
- Customers on month-to-month contracts show the highest churn
- Churn rate is higher among customers with shorter tenure
- Fiber optic internet users churn more compared to DSL users
- Electronic check payment method has higher churn presence

## Dashboard Features
- KPI cards for total customers, churned customers, retained customers, and churn rate
- Interactive slicers for gender, senior citizen, contract type, and internet service
- Churn analysis by contract, tenure, internet service, and payment method
- Tables summarizing churn distribution and revenue impact

## Tools & Technologies Used
- Power BI
- DAX
- Power Query
- Data Cleaning & Visualization

##[Telco Customer Churn Dashboard](telco_churn_dashboard.png)

## Conclusion
This project helped me strengthen my Power BI skills, especially in data modeling, DAX calculations, and dashboard design. The dashboard provides clear insights into churn behavior and can help businesses take data-driven decisions to improve customer retention.



