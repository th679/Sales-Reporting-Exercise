import csv

csv_file_path = "data.csv"

product_sales =[]

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        d = {"date": ["date"], "product": row["product"], "unit price": row["unit price"], "units sold": row["units sold"], "sales price": float(row["sales price"])}
        product_sales.append(d)

print("SALES REPORT (MONTH YEAR)")

total_sales = 0

for p in product_sales:
    total_sales = total_sales + p["sales price"]

total_sales_usd = "${0:,.2f}".format(total_sales,)

print("TOTAL SALES: " + total_sales_usd)