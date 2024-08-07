## Brief Description
Your task is to investigate and resolve a bug in an existing Python function designed to manipulate strings by reversing substrings enclosed in parentheses. 

All the code should be put inside the given function template `reverse_substrings` from the `solution` module.

## Function Description
The provided function, reverse_substrings, takes a single string as input. This string can contain several substrings enclosed in parentheses, possibly nested. The function is supposed to reverse each substring found within the parentheses, handling nested structures from the innermost to the outermost level.

### Known Issue
The function has a known issue with handling cases of nested parentheses and may not correctly reverse substrings as expected, especially in complex scenarios.

## Expected Sequence of Steps

- Identify the bug in the function that leads to incorrect handling of nested parentheses.
- Correct the code so that it functions as intended, which includes correctly reversing substrings within all levels of nested parentheses.

## Deliverables
- A modified version of the reverse_substrings function that correctly handles all specified cases.