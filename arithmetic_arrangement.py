def arithmetic_arranger(problems,show_results=False):
    number_of_problems = len(problems)
    seperated_part = [problem.split(" ") for problem in problems]
    operators = [list[1] for list in seperated_part];
    operands = [[list[0],list[2]] for list in seperated_part];
    digits_string="0123456789"
    
    # print(number_of_problems,"problems :",seperated_part);
    # print("Operators : "+(' '.join(operators)));
    # print("Operands :",operands);

    # 1.Check all the situations that will run errors
    # Check length : can't more than 5 problems
    if(number_of_problems > 5 ): 
        return "Error: Too many problems."

    # Check operator : Operator must be '+' or '-'
    if (("*" in operators) or ("/" in operators)) :
        return "Error: Operator must be '+' or '-'."

    # Check operand : must only contain digits
    for operand_list in operands:
        for character in operand_list[0]:
            if not (character in digits_string):
                return "Error: Numbers must only contain digits."
        for character in operand_list[1]:
            if not (character in digits_string):
                return "Error: Numbers must only contain digits."
        # Check operand : can't be more than four digits
        if(len(operand_list[0])>4 or len(operand_list[1])>4):
            return "Error: Numbers cannot be more than four digits."

    # 2.If the user supplied the correct format of problems
    result_lines =  {
        1:[],
        2:[],
        3:[],
        4:[]
    }

    # Struct each problem
    for i in range(number_of_problems):
        first,second = operands[i]
        longest = max(len(first),len(second))
        space = longest+2
        operator = operators[i]
        calculation = str(int(first)+int(second)) if operator=="+" else str(int(first)-int(second))
        if (show_results):
            if (i<number_of_problems-1):
                result_lines[1] = result_lines[1] + ["  "+" "*(longest-len(first))+first+" "*4]
                result_lines[2] = result_lines[2] + [operators[i]+" "+" "*(longest-len(second))+second+" "*4]
                result_lines[3] = result_lines[3] + ["-"*space+" "*4]
                result_lines[4] = result_lines[4] + [" "*(space-len(calculation))+calculation+" "*4]
            else:
                result_lines[1] = result_lines[1] + ["  "+" "*(longest-len(first))+first+"\n"]
                result_lines[2] = result_lines[2] + [operators[i]+" "+" "*(longest-len(second))+second+"\n"]
                result_lines[3] = result_lines[3] + ["-"*space+"\n"]
                result_lines[4] = result_lines[4] + [" "*(space-len(calculation))+calculation]
        else:
            if (i<number_of_problems-1):
                result_lines[1] = result_lines[1] + ["  "+" "*(longest-len(first))+first+" "*4]
                result_lines[2] = result_lines[2] + [operators[i]+" "+" "*(longest-len(second))+second+" "*4]
                result_lines[3] = result_lines[3] + ["-"*space+" "*4]
            else:
                result_lines[1] = result_lines[1] + ["  "+" "*(longest-len(first))+first+"\n"]
                result_lines[2] = result_lines[2] + [operators[i]+" "+" "*(longest-len(second))+second+"\n"]
                result_lines[3] = result_lines[3] + ["-"*space]

    if show_results == True :
        results = result_lines[1]+result_lines[2]+result_lines[3]+result_lines[4]
        return "".join(results)
    else:
        results = result_lines[1]+result_lines[2]+result_lines[3]
        return "".join(results)


# problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "108 - 45"]
problems = ['3801 - 2', '123 + 49']
print(arithmetic_arranger(problems))
print('  3801      123\n-    2    +  49\n------    -----' == arithmetic_arranger(problems))