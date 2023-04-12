import pandas as pd

# Create a dictionary with the data to be uploaded
data = {'Name': ['John', 'Alice', 'Bob', 'Jane'], 'Age': [25, 28, 30, 35], 'Salary': [50000, 60000, 70000, 80000]}

# Create a Pandas dataframe from the dictionary
df = pd.DataFrame(data)

# Write the dataframe to an Excel file with columns as headers
df.to_excel('output.xlsx', index=False)
