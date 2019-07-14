number_of_sums = int(input())

sums = [int(input()) for x in range(number_of_sums)]

def generate_equation(given_sum):
    allowed_operations = "* + - //".split(' ')

    equation_form = "4 {} 4 {} 4 {} 4 == {}"

    for operation_1 in allowed_operations:
        for operation_2 in allowed_operations:
            for operation_3 in allowed_operations:
                tmp_equation = equation_form.format(
                    operation_1,
                    operation_2,
                    operation_3,
                    given_sum
                )
                if eval(tmp_equation):
                    return tmp_equation.replace('==', '=').replace('//', '/')
    return 'no solution'

for s in sums:
    print(generate_equation(s))
