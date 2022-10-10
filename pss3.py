import csv 

def get_students(filename, first_name):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        section = 0
        student_list = []

        for line in csv_reader:
            if first_name in line[0]:
                section = line[1]

        file.seek(0)

        for line in csv_reader:
            if line[1] == section:
                student_list.append(line[0]) 
        
        return student_list

if __name__ == '__main__':
    print(get_students('grades.csv', 'tom'))
    
    