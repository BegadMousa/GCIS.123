import re
import csv

def zip_check(filname):
    with open(filname) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for rows in csv_reader:
            if re.findall(r'^[7,8,9]\d{4}$', rows[2]):
                print(f'found a match! ,{rows[2]}')
            else:
                print('no match')


def main():
    zip_check('zipcodes.csv')

if __name__ == '__main__':
    main()