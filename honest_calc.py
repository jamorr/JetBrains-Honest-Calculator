import sys
memory = 0

#returns True if input is a single digit
def is_one_digit(v) -> bool:
    if type(v) == float and v.is_integer() and abs(int(v)) < 10:
        return True
    else:
        return False


def isnt_float(num:str) -> bool:
    #return false if float
    try:
        float(num)
        return False
    except ValueError:
        return True


def store_check(index1: int, result):
    msg_list = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]
    print(msg_list[index1])
    answer = input()
    if answer == 'y':
        if index1 < 2:
            index1 +=1
            store_check(index1, result)
        else:
            global memory
            memory = result
    elif answer != 'n':
        store_check(index1, result)


def store(input1):
    print("Do you want to store the result? (y / n):")
    answer = input()
    if answer == 'y':
        if is_one_digit(input1):
            msg_ind = 0
            store_check(msg_ind, input1)
        else:
            global memory
            memory = input1
    elif answer != 'n':
        store(input1)


def repeat(input2):
    print("Do you want to continue calculations? (y / n):")
    answer = input()
    if answer == 'y':
        main()
    elif answer != 'n':
        repeat(input2)
    else:
        sys.exit()

#prints how lazy person is
def lazy(input4: tuple) -> tuple:
    msg = ''
    msg_list = [" ... lazy", " ... very lazy",
                " ... very, very lazy", "You are"]
    v1, v3, v2 = input4
    #test
    #print(v1, v3, v2)


    #print(is_one_digit(v1),is_one_digit(v2))
    #if either input is one dig
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_list[0]
        #if multiplying by 1
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_list[1]
        #if mult or adding 0
    if (v1 == 0 or v2 == 0) and v3 in ['+','-','*']:
         msg += msg_list[2]
    #prepend you are and print
    if msg != '':
        msg = msg_list[3] + msg
        print(msg)
    return input4

def perf_oper(input: tuple) -> object:
    #perform operation on input if possible
    x, oper, y = input
    if oper == '+':
        out = x + y
        print(out)
    elif oper == '-':
        out = x - y
        print(out)
    elif oper == '*':
        out = x * y
        print(out)
    elif y != 0:
        out = x / y
        print(out)
    else:
        print("Yeah... division by zero. Smart move...")
        main()
    return out


def input_eq():
    print("Enter an equation")
    user_input = input()
    a, var, b = user_input.split(' ')
    #check if memory var is called
    if a == 'M':
        a = memory
    if b == 'M':
        b = memory
    #check if float
    if (isnt_float(a) or isnt_float(b)):
        print("Do you even know what numbers are? Stay focused!")
        return input_eq()
    #check if valid operator
    if var not in ['+', '-', '*', '/']:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return input_eq()
    return float(a), var, float(b)

def main():
    return repeat(store(perf_oper(lazy(input_eq()))))

main()

