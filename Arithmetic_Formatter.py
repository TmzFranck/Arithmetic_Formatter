def arithmetic_arranger(problems, show_answers=False):
    line1 = ''
    line2 = '\n'
    line3 = '\n'
    line4 = '\n'
    result = 0
    x = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for i in range(len(problems)):
        x, operator, y = problems[i].split(" ")
        max_len = max(len(x), len(y))
        if operator is '*' or operator is '/':
            return "Error: Operator must be '+' or '-'."
        elif not x.isdigit() or not y.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(x) > 4 or len(y) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if operator == '+':
            result = int(x) + int(y)
        else:
            result = int(x) - int(y)
        
        line1 += f'{x.rjust(max_len + 2)}' + (('    ') if i < len(problems) - 1 else '')
        line2 += f'{operator}' + ' ' + f'{y.rjust(max_len)}' + (('    ') if i < len(problems) - 1 else '')
        line3 += '-' * (max_len + 2) + (('    ') if i < len(problems) - 1 else '')
        line4 += f'{str(result).rjust(max_len + 2)}' + (('    ') if i < len(problems) - 1 else '')   
    return line1 + line2 + ((line3 + line4) if show_answers else line3)


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

formatted_problems_with_answers = arithmetic_arranger(problems, True)

print(formatted_problems_with_answers)