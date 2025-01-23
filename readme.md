# Simple Language Interpreter

This project is a simple interpreter for a custom language. It supports basic arithmetic operations, variable assignments, and input/output operations.

## Features

- **Variable Assignment**: Assign values to variables.
- **Arithmetic Operations**: Perform basic arithmetic operations like addition, subtraction, multiplication, and division.
- **Input/Output**: Take user input and print output.
- **Custom Data Types**: Supports custom integer, float, and string types.

## Usage

1. **Clone the repository**:

    ```sh
    git clone https://github.com/SarveshCA/sarvlang-simple-interpreter.git
    cd sarvlang-simple-interpreter
    ```

2. **Run the interpreter**:

    ```sh
    python main.py program.sarv
    ```

## Example Programs

### Variable Assignment

```sarv
START
    oye sun a = 10
    oye sun b = 20
    oye sun c = 'Hello'
STOP
```

### Arithmetic Operations

```sarv
START
    oye sun a = 10
    oye sun b = 20
    oye sun sum = {a + b}
    oye sun difference = {a - b}
    oye sun product = {a * b}
    oye sun quotient = {a / b}
    oye sun modulus = {a % b}
    oye sun exponent = {a ** 2}
    oye sun floordiv = {a // 3}
STOP
```

### Input/Output

```sarv
START
    a lele 'Enter a: '
    b lele 'Enter b: '
    ye print kar 'You entered a = {a} and b = {b}'
STOP
```

### Custom Data Types

```sarv
START
    oye sun int_var = 10
    oye sun float_var = 10.5
    oye sun string_var = 'Hello World'
    ye print kar 'Integer: {int_var}, Float: {float_var}, String: {string_var}'
STOP
```

### Combined Example

```sarv
START
    oye sun a = 10
    oye sun b = 20
    oye sun c = 'Result'
    oye sun sum = {a + b}
    ye print kar '{c}: {sum}'
    a lele 'Enter a new value for a: '
    ye print kar 'New value of a: {a}'
STOP
```

## File Descriptions

- **main.py**: The main interpreter code.
- **program.sarv**: An example program written in the custom language.

## How It Works

1. **Memory Class**: Manages variable storage.
2. **Custom Data Types**: `apnaInt`, `apnaFloat`, and `apnaString` classes for handling different data types.
3. **Expression Evaluation**: `evaluate_expression` function to evaluate arithmetic expressions.
4. **Custom Evaluation**: `custom_eval` function to handle operator precedence and evaluation.
5. **Interpreter Logic**: `run_sarv` function to parse and execute the custom language commands.

## Future Improvements

- Add support for loops and conditionals.
- Improve error handling and reporting.
- Expand the set of supported operations and data types.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License.
