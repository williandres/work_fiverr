import csv
import os

def new_csv(f):
    print(f)

def read_csv(file_name):
    with open(f"{file_name}","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittle = next(reader)
        file = []
        for row in reader:
            file.append(row)
    return file

def main():
    old_csv = read_csv('GJI - OCT NOV DIC.xlsx - Original.csv')
    new_csv(old_csv)
if __name__ == '__main__':main()