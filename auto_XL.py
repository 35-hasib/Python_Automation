import pandas as pd

# Function to read an Excel file and return a DataFrame
def read_excel_file(file_path, sheet_name='Sheet1'):
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Function to write a DataFrame to an Excel file
def write_to_excel_file(data_frame, file_path, sheet_name='Sheet1'):
    with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
        data_frame.to_excel(writer, sheet_name=sheet_name, index=False)

# Example usage
df_members = read_excel_file('members.xlsx')
print(df_members)


# Write the updated DataFrame back to the Excel file
write_to_excel_file(df_members, 'members.xlsx')
