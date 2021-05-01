import math

def solution_1_divide_by_10(number):
    """
        Divide the number by 10 till it becomes zero. Number of iteration is the result. 
    """
    count = 0

    while number > 0:
        number = int(number / 10)
        count = count + 1

    return count

def solution_2_recursive(number):
    
    if number == 0:
        return 0

    number = int(number / 10)
    return 1 + solution_2_recursive(number)

def solution_3_log_base_10(number):
    return int(math.log10(number)) + 1     

print(f'solution 1 result - {solution_1_divide_by_10(12345)}')
print(f'solution 2 result - {solution_2_recursive(12345)}')
print(f'solution 3 result - {solution_3_log_base_10(12345)}')

