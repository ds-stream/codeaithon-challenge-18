### YOUR TASK IS TO MODIFY THIS CODE TO WORK
def reverse_substrings(input_string):
    """
    Reverses substrings in a string that are enclosed in parentheses. Nested parentheses are handled
    from the innermost to the outermost level.
    
    Args:
    input_string (str): The input string containing zero or more pairs of parentheses.
    
    Returns:
    str: A string with the substrings reversed between each pair of parentheses.
    """
    import re

    paren_pair_regex = r'\([^\(\)]*\)'

    while '(' in input_string:
        matches = re.findall(paren_pair_regex, input_string)

        for match in matches:
            inner_text = match[1:-1] 
            reversed_text = inner_text[::-1]
            input_string = input_string.replace(match, reversed_text, 1)

    return input_string

# Example usage:
print(reverse_substrings("Example (string)"))  # "Example gnirts"
print(reverse_substrings("(abc(def)ghi)"))  # "ihgfedcba", should handle nesting but doesn't correctly
