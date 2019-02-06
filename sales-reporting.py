import csv

csv_file_path = "data.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)


print("SALES REPORT (MONTH YEAR)")
