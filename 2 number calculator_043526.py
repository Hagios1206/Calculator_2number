# to condition the loop such that it must be a digit
def command():
    while True:
        x = input("insert your first number: ")
        if x .isdigit():  #note you have to use function before condition
            x = float(x) 
        else:
            print("Error! insert a valid number")
            continue
        break
    while True:
        y = input("Insert your second number: ")
        if y .isdigit():
            y = float(y)
        else:
            print("Error! insert a valid number")
            continue
        break
#the only thing we are concerned about
    return(x,y)

def sum(x,y):
    total = x + y
    print(f"{x} + {y} = {total}")

def subtraction(x,y):
    total = x - y
    print(f"{x} - {y} = {total}")

def multiply(x,y):
    total = x * y
    print(f"{x} * {y} = {total}")

def division(x,y):
    total = x / y
    print(f"{x} / {y} = {total:.2f}")



print("insert: \n sum   #To perform addition(+) \n sub   #To perform subtraction(-)" +
"\n mul   #To perform multiplication(*) \n div   #To perform division(/)" +
"\n q     #To quit" )

while True:
    pull =input("\nChoose your operation (sum/sub/div/mul/q):  ").strip().lower()
    if pull == "sum":
        x,y = command()
        sum(x,y)
    elif pull == "sub":
        x,y = command()
        subtraction(x,y)
    elif pull == "mul":
        x,y = command()
        multiply(x,y)
    elif pull =="div":
        x,y = command()
        division(x,y)
    elif pull == "q":
        print("\n ....Exiting calculator....\n")
        quit()
    else:
        print("\n Error! Error!! choose a valid operation")

