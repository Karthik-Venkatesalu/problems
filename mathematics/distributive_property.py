"""
Distributive property is one of the rule in maths that helps to solves the expressions like x(y + z) form. 
We can apply this rule to solve addition and subtraction problems.

Programatically, it can be represented as below.

x * sum(terms) = sum(x * terms[0] + x * terms[1] + ... + x * terms[n - 1])

x is the multiplicative constant which can be moved in and out of the sums.

Same can be applied to division as well.

"""
def distributive_property_of_multiplication(numbers): 
    sum = 0
    multiplicative_constant = 2

    for n in numbers:
        sum = sum + n
    
    solution_1 = multiplicative_constant * sum

    solution_2 = 0
    for n in numbers:
        solution_2 = solution_2 + (n * multiplicative_constant)

    
    print(f'LHS == RHS - {solution_1 == solution_2}')

distributive_property_of_multiplication([4, 5, 6])
