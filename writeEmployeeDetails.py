import pandas as pd

def writeEmpDetails():
# Create a data  with student details
    employee_details = pd.DataFrame(
    {"ID": [1, 2, 3, 4], "Name": ["Vardhan", "Praveen", "Bhanu", "Raju"]}
    )
# Write the data to a CSV file
    employee_details.to_csv("employee_details.csv", index=False)

    print("Employee details written to employee_details.csv")
