## Brief Description
In this task, participants are required to debug and fix a non-working function named `reverse_substrings`. The function is designed to take a string as input and return a new string where each word's characters are reversed while preserving the order of words and spaces. Participants will need to identify and correct the existing bugs in the function and ensure that it passes all the provided test cases.

All the code should be put inside the given function template `reverse_substrings` from the `solution` module.

## Function Description
`reverse_substrings(s: str) -> str`
Input: A single string s, consisting of words separated by spaces. The string may include punctuation and various amounts of whitespace.

Output: A new string where each word in the input string is reversed, but the order of the words and spaces between them are preserved.

Example:
- Input: "hello world"
- Output: "olleh dlrow"

### Known Issue
The function has a known issue and may not correctly reverse substrings as expected, especially in complex scenarios.

## Expected Sequence of Steps

- Identify the bug in the function that leads to incorrect results.
- Correct the code so that it functions as intended, which includes correctly reversing substrings.

## Deliverables
- A modified version of the reverse_substrings function that correctly handles all specified cases.