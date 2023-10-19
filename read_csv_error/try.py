import pandas as pd

file_csv = "sources/Main_data.csv"

cods = ["utf-8", "iso-8859-1", "windows-1252", "latin-1"]

for cod in cods:
    try:
        with open(file_csv, "r", encoding=cod) as file:
            final_rows = []
            for line in file:
                try:
                    row = line.strip().split("\t")
                    final_rows.append(row)
                except Exception as e:
                    print(f"Error on row: {line}")
                    print(f"Error details: {e}")
        df1 = pd.DataFrame(final_rows)
        break
    except UnicodeDecodeError:
        continue
else:
    print("Impossible to read")

print(df1.head(10))
print(df1.tail(10))


