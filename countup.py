from ast import Num


def main():
    num = int(input("Please enter a number: "))
    sum =0
    while(num>=0):
        print(num)
        sum += num
        num -= 1
    print(f"Sum = {sum}")

if __name__ == "__main__":
    main()