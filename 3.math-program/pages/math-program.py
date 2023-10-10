def sum(first , second):
    print(f"Summation result is : {first + second}")


def subtraction(first , second):
    return first - second


def multiplication(first , second , third , fourth):
    multiply = first * second * third * fourth
    print(f"Summation result is : {multiply}")
    return multiply


def division(first , second):
    divide = first / second
    modulus = first % second

    if modulus != 0 :
        return modulus
   
    return divide
    



sum(3 , 6)
subtraction_result = subtraction(100 , 34)
print(f"Subtraction result is : {subtraction_result}")
multiplication(12 , 13 , 14 , 15)
divide_value = division(21 , 4)
print(divide_value)