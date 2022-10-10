import csv

def class_average(filename, section, grade_item):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        total = 0
        count = 0
        for line in csv_reader:
            if line[1] == section:
                total += int(line[grade_item+2])
                count += 1
        return total / count


if __name__ == '__main__':
    # class_average('grades.csv', '2', 6)
    print(f'Section average : {class_average("grades.csv", "2", 6)}')