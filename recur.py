from re import M


def my_func(a):
    if a<10:
        a+=1
        print(a," iteration")
        my_func(a)

def countdown(number):
    if number <0 :
        return
    elif number == 0:
        print(number)
        return 0
    else:
        print(number)
        return number + countdown(number-1)
    

def main():
    # x=0
    print("sum : ", countdown(10))
    
 
if __name__ == "__main__":
    main()

