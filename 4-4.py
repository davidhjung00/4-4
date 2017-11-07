"""
2017/11/06

This program is for counting the number of cases to meet the following condition

Input : 4x4 matrix
value : between 0 - 2

1. sum for each row is 3
2. sum for each column is 3

I get the number using direct programming.

David H Jung  
"""
MAX_SIZE  = 16
ROW_SIZE = 4
TARGET_SUM = 3
def isRight(value) :
    # for each row
    for i in range (ROW_SIZE) :
        sum = 0
        for j in range(ROW_SIZE) :
            sum += value[i*ROW_SIZE+j]
        if sum != TARGET_SUM :
            return 0
    # for each column
    for i in range (ROW_SIZE) :
        sum = 0
        for j in range(ROW_SIZE) :
            sum += value[i+ROW_SIZE*j]
        if sum != 3 :
            return 0

    return 1

# print out the current value as a form of matrix
def print_current(value) :
    global correct
    print("[", correct, "]")
    for i in range(ROW_SIZE):
        print("(", value[i*ROW_SIZE+0], ",", value[i*ROW_SIZE+1], ",", value[i*ROW_SIZE+2], ",", value[i*ROW_SIZE+3], ")")

def do_it(value, cur) :
    global correct
    if ( cur >= MAX_SIZE) :
        return 0
    for i in range(3) :
        value[cur] = i
        if ( cur == MAX_SIZE -1 ) :
            if (isRight(value)) :
                print_current(value)
                correct += 1
        do_it(value, cur+1)

    value[cur] = 0

value = [0  for row in range(MAX_SIZE)]
correct = 0

do_it(value, 0)
print ("correct : ", correct )

