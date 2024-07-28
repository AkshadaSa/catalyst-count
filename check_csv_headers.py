import os

file_path = r'C:\Users\Admin\Downloads\free-7-million-company-dataset\companies_sorted.csv'
if os.path.isfile(file_path):
    print("File exists.")
else:
    print("File does not exist.")
