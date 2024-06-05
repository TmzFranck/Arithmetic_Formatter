# Arithmetic Formatter

## Project Overview
The Arithmetic Formatter project is a tool that takes a list of simple arithmetic problems and formats them in a visually appealing manner. This project is designed to help users practice arithmetic problems, presenting the equations in a structured and easy-to-read format.

## Features
- Accepts a list of arithmetic problems involving addition and subtraction.
- Supports problems with multiple digits.
- Aligns the problems vertically and horizontally.
- Provides an option to display or hide the answers.

## Installation
To get started with the Arithmetic Formatter project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TmzFranck/Arithmetic_Formatter.git
   ```
2. Navigate to the project directory:

    ```bash
    cd Arithmetic_Formatter
    ```

## Usage
The Arithmetic Formatter can be used by calling the arithmetic_arranger function. Below is an example of how to use the function:

Example
```python
from arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted_problems = arithmetic_arranger(problems)
print(formatted_problems)

# With answers
formatted_problems_with_answers = arithmetic_arranger(problems, True)
print(formatted_problems_with_answers)
``` 

# Output

```diff

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

With the solve parameter set to True:

```diff

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```