import pandas as pd

file_csv = "Main_data.csv"

with open(file_csv, "r", encoding="latin-1") as file:
    final_rows = []
    for line in file:
        row = line.strip().split("\t")
        final_rows.append(row)
df1 = pd.DataFrame(final_rows)


print(df1.head(10))
print(df1.tail(10))


