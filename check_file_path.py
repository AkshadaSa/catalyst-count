import os

file_path = r'C:\Users\Admin\Downloads\free-7-million-company-dataset\companies_sorted.csv'
print(f"Checking if file exists: {file_path}")
if os.path.isfile(file_path):
    print("File found!")
else:
    print("File not found.")
