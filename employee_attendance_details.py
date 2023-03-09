import pandas as pd

# Define the data to be stored in the CSV file
data = {"ID": [], "Attendance": []}

# Create a DataFrame from the data
employee_attendance = pd.DataFrame(data)

# Write the DataFrame to a CSV file
employee_attendance.to_csv("employee_attendance.csv", index=False)
