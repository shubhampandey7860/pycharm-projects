import csv
def main():
    f=open('Employee.csv','r',newline='')
    r=csv.reader(f)
    for row in r:
        print(row)
    f.close()
main()
