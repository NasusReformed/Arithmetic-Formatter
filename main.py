def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."
        
        #Variables 
        num1, operator, num2 = parts
        
        #Condicionales
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Espacio para el operador y al menos un espacio
        width = max(len(num1), len(num2)) + 2  
        
        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes.append("-" * width)
        
        if display_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))
    
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)
    
    if display_answers:
        arranged_problems += "\n" + "    ".join(results)
    
    return arranged_problems

# Pruebas de ejemplo
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))