import csv 

def name_address(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            print(line[0], line[1])
