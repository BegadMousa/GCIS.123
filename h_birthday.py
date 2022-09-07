from webbrowser import get


'''
    This program is done as the first part of the class work week 2 GCIS 123
'''

def b_day():
    name = input("What is your name?: ")
    month = input("What month were you born in?: ")
    day = input("What day were you born on?: ")
    year = input("What year were you born in?: ")

    print(f'Hello {name}! your birthday is on {day},{month},{year}!\n\n')  

def addition():
    num1 = int(input("Enter A Number: "))
    num2 = int(input("Enter Another Number: "))
    print(f"result= {num1 + num2}")

def main():
    print("\n")
    for i in range(3):
        b_day()

    addition()
        
if __name__ == "__main__":
    main()