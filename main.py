import sys

class Memory:
    def __init__(self):
        self.data = {}
    
    def __setattr__(self, variable_name: str, variable_value: object):
        if variable_name == 'data':
            super().__setattr__(variable_name, variable_value)
        else:
            self.data[variable_name] = variable_value
    
    def add_variable(self, variable_name: str, variable_value: object):
        self.data[variable_name] = variable_value

    def __getattr__(self, variable_name: str):
        if variable_name == 'data':
            super().__getattr__(variable_name)
        else:
            return self.data[variable_name]

    def has_variable(self, variable_name: str):
        return variable_name in self.data
        
    def __call__(self, variable_name: str, variable_value: object):
        self.data[variable_name] = variable_value

    def __setitem__(self, variable_name: str, variable_value: object):
        self.data[variable_name] = variable_value

    def __getitem__(self, variable_name):
        return self.data[variable_name]

class apnaInt:
        def __init__(self, value):
            self.value = int(value)
        
        def __repr__(self):
            return str(self.value)
        
        def __str__(self):
            return str(self.value)
        
        def __add__(self, other_int: object):
            if isinstance(other_int, apnaInt):
                return apnaInt(str(int(self.value) + int(other_int.value)))
            else:
                return 'error'

        def __sub__(self, other_int: object):
            if isinstance(other_int, apnaInt):
                return apnaInt(str(int(self.value) - int(other_int.value)))
            else:
                return 'error'

class apnaFloat:
        def __init__(self, value):
            self.value = float(value)
        
        def __repr__(self):
            return str(self.value)
        
        def __str__(self):
            return str(self.value)
        
        def __add__(self, other_int: object):
            if isinstance(other_int, apnaInt):
                return apnaInt(str(float(self.value) + float(other_int.value)))
            else:
                return 'error'

        def __sub__(self, other_int: object):
            if isinstance(other_int, apnaInt):
                return apnaInt(str(float(self.value) - float(other_int.value)))
            else:
                return 'error'
            
class apnaString:
        def __init__(self, value):
            self.value = value
        
        def __repr__(self):
            return str(self.value)
        
        def __str__(self):
            return str(self.value)
        
        def __add__(self, other_int: object):
            if isinstance(other_int, apnaString):
                return apnaString(str(int(self.value) + int(other_int.value)))
            else:
                return 'error'

def custom_eval(tokens):
    if not tokens:
        return 'error'
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '**': 3, '//': 2}
    right_associative = {'**'}
    output_queue = []
    operator_stack = []

    for token in tokens:
        if isinstance(token, (apnaInt, apnaFloat, apnaString)):
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] in precedence and
                   ((token not in right_associative and precedence[token] <= precedence[operator_stack[-1]]) or
                    (token in right_associative and precedence[token] < precedence[operator_stack[-1]]))):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            return 'error'
    
    while operator_stack:
        output_queue.append(operator_stack.pop())

    stack = []
    for token in output_queue:
        if isinstance(token, (apnaInt, apnaFloat, apnaString)):
            stack.append(token)
        elif token in precedence:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            b = b.value if isinstance(b, (apnaFloat, apnaInt)) else b
            a = stack.pop()
            a = a.value if isinstance(a, (apnaFloat, apnaInt)) else a
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "%":
                stack.append(a % b)
            elif token == "**":
                stack.append(a ** b)
            elif token == "//":
                stack.append(a // b)
        else:
            return 'error'
    
    return stack[0] if len(stack) == 1 else 'error'

def evaluate_expression(expression, memory, line_count):
    operators = {"+", "-", "*", "/", "%", "**", "//"}
    current_value = ""
    tokens = []

    i = 0
    while i < len(expression):
        char = expression[i]
        if char in operators:
            if i + 1 < len(expression) and expression[i:i+2] in {'**', '//'}:
                char = expression[i:i+2]
                i += 1
            if current_value:
                current_value = current_value.strip()
                if '.' in current_value and current_value.count('.') == 1:
                    number, decimal = current_value.split('.')
                    if number.isdigit() and decimal.isdigit():
                        tokens.append(apnaFloat(current_value))
                elif current_value.isdigit():
                    tokens.append(apnaInt(current_value))
                elif current_value.startswith("'") and current_value.endswith("'"):
                    tokens.append(apnaString(current_value.strip("'")))
                elif current_value in memory.data:
                    if isinstance(memory[current_value], apnaInt):
                        tokens.append(memory[current_value])
                    elif isinstance(memory[current_value], apnaFloat):
                        tokens.append(memory[current_value])
                    elif isinstance(memory[current_value], apnaString):
                        tokens.append(memory[current_value])
                else:
                    print(f"Line {line_count}: Error: '{current_value}' is not defined.")
                    return False
            tokens.append(char)
            current_value = ""
        else:
            current_value += char
        i += 1

    if current_value:
        current_value = current_value.strip()
        if '.' in current_value and current_value.count('.') == 1:
            number, decimal = current_value.split('.')
            if number.isdigit() and decimal.isdigit():
                tokens.append(apnaFloat(current_value))
        elif current_value.isdigit():
            tokens.append(apnaInt(current_value))
        elif current_value.startswith("'") and current_value.endswith("'"):
            tokens.append(apnaString(current_value.strip("'")))
        elif current_value in memory.data:
            if isinstance(memory[current_value], apnaInt):
                tokens.append(memory[current_value])
            elif isinstance(memory[current_value], apnaFloat):
                tokens.append(memory[current_value])
            elif isinstance(memory[current_value], apnaString):
                tokens.append(memory[current_value])
        else:
            print(f"Line {line_count}: Error: '{current_value}' is not defined.")
            return False

    return custom_eval(tokens) if len(tokens)>=2 else tokens[0]

def assignDataType(value):
    if isinstance(value, int):
        return apnaInt(value)
    elif isinstance(value, float):
        return apnaFloat(value)
    elif isinstance(value, str):
        return apnaString(value)
    elif isinstance(value, apnaInt) or isinstance(value, apnaFloat) or isinstance(value, apnaString):
        return value
    else:
        return False
    
def get_code(filename: str) -> list:
    f : object = open(filename)
    code = f.readlines()
    f.close()
    return code

def run_sarv(filename: str) -> bool:
    code: list[str] = get_code(filename)
    start_flag = False
    variable_name = None
    for line_count in range(len(code)):
        if code[line_count].startswith('START'): 
            start_flag = True
            _memory = Memory()
            continue

        if not start_flag:
            continue

        if code[line_count].startswith('STOP'): 
            start_flag = False
            return True
        
        current_line = code[line_count]
        current_line = current_line.strip()
        if current_line == '':
            continue

        ## COMMENTS
        if current_line.startswith('//'):
            continue

        ## PRINT
        PRINT_COMMAND = 'ye print karo'
        if current_line.startswith(PRINT_COMMAND):
            _, content_to_print = current_line.split(PRINT_COMMAND)
            content_to_print = content_to_print.strip()

            if (content_to_print[0] == "\'" and content_to_print[-1] != "\'") or (content_to_print[0] != "\'" and content_to_print[-1] == "\'"):
                    print(f'\nError on line {line_count+1}: String not used correctly.')
                    return False
            
            content_to_print = content_to_print[1:-1]

            elements = []
            element_type = {}
            element_index = 0
            content_packet = ''
            var_flag = False
            for i in range(len_:=len(content_to_print)):
                if (not var_flag) and content_to_print[i] == '{':
                    var_flag = True
                    if content_packet != '':
                        elements.append(content_packet)
                        element_type[str(element_index)] = 'string_literal'
                        element_index+=1
                    content_packet = ''
                    continue

                if var_flag and content_to_print[i] == '}':
                    var_flag = False
                    elements.append(content_packet)
                    element_type[str(element_index)] = 'expression'
                    element_index+=1
                    content_packet=''
                    continue
                
                if i == len_ - 1 and content_to_print[i] != '}' and var_flag:
                    print(f'\nError on line {line_count+1}: \'{{\' is not closed properly')
                    return False

                content_packet += content_to_print[i]
                
                if i == len_ - 1 and (not var_flag):
                    elements.append(content_packet)
                    element_type[str(element_index)] = 'string_literal'
            for i in range(len(elements)):
                if element_type[str(i)] == 'string_literal':
                    print(elements[i], end='')
                elif element_type[str(i)] == 'expression':
                    result = evaluate_expression(elements[i], _memory, line_count)
                    if result is False:
                        return False
                    print(result, end='')
                else:
                    pass
            print('\n', end='')
            continue

        ## INPUT
        INPUT_COMMAND = 'lelo'
        if INPUT_COMMAND in current_line:
            variable_name_by_user, content_to_display = current_line.split(INPUT_COMMAND)
            content_to_display = content_to_display.strip()
            variable_name_by_user = variable_name_by_user.strip()
            if content_to_display == '':
                content_to_display = '\'\''
            if (content_to_display[0] == "\'" and content_to_display[-1] != "\'") or (content_to_display[0] != "\'" and content_to_display[-1] == "\'"):
                print(f'Error on line {line_count+1}: String not used correctly.')
                return False
            else:
                if content_to_display[0] == "\'" and content_to_display[-1] == "\'":
                    user_input = input(content_to_display[1:-1])
                    user_input = evaluate_expression(user_input, _memory, line_count)
                    if (res:=assignDataType(user_input)) is not False:
                        _memory[variable_name] = res
                    else:
                        print(f'Error on line {line_count+1}: Unsupported result type.')
                    _memory[variable_name_by_user] = user_input
                    continue
            continue

        ## Variables
        INPUT_COMMAND = 'oye suno'
        if INPUT_COMMAND in current_line:
            _, command_ = current_line.split(INPUT_COMMAND)
            variable_name, variable_value = list(map(lambda x: x.strip(), command_.strip().split('=')))
            if variable_name == '' or variable_value == '':
                print(f'Error on line {line_count+1}: \'=\' not use properly')
                return False
            
            if len(variable_value)<2:
                variable_value += ' '
            
            if (variable_value[0] == "\'" and variable_value[-1] != "\'") or (variable_value[0] != "\'" and variable_value[-1] == "\'"):
                print(f'Error on line {line_count+1}: String not used correctly.')
                return False
            else:
                if variable_value[0] == "\'" and variable_value[-1] == "\'":
                    user_input = apnaString(variable_value[1:-1])
                    _memory[variable_name] = user_input
                    continue
                elif all([i not in variable_value for i in ['+', '-', '*', '/', '//', '%','**']]):
                    variable_value = variable_value.strip()
                    try:
                        if '.' in variable_value and variable_value.count('.') == 1:
                            user_input = apnaFloat(variable_value)
                        else:
                            user_input = apnaInt(variable_value)
                    except ValueError:
                        print(f'Error on line {line_count+1}: Invalid value.')
                        return False
                    except Exception as e:
                        print(f'Error on line {line_count+1}: {e}.')
                        return False
                    _memory[variable_name] = user_input
                    continue
                else:
                    try:
                        print(variable_value)
                        result = evaluate_expression(variable_value, _memory, line_count)
                        if (res:=assignDataType(result)) is not False:
                            _memory[variable_name] = res
                        else:
                            print(f'Error on line {line_count+1}: Unsupported result type.')

                    except NameError as e:
                        print(f'Error on line {line_count+1}: {str(e)}')
                        return False
                    except SyntaxError as e:
                        print(f'Error on line {line_count+1}: Syntax error in expression.')
                        return False
                    except Exception as e:
                        print(f'Error on line {line_count+1}: {str(e)}')
                        return False

                    continue
                    

        print(f'Error on line {line_count+1}: This line is useless.')
        return False

    return True

def main():
    if (arg_len := len(sys.argv)) < 2:
        print('Not sufficient arguments.')
        return
    if arg_len > 2:
        print('More than expected arguments.')
        return
    if sys.argv[-1][::-1].split('.')[0][::-1] != 'sarv':
        print('You can only run a .sarv file with this command')
        return
    script_name :str = sys.argv[1]
    print(f"Executed file: {script_name}\n----------------------------------------")
    exit_value = run_sarv(script_name)
    print(f'----------------------------------------\nCode exited with value {exit_value}')

if __name__ == "__main__":
    main()