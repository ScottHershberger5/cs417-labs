"""
JSON Structure Validator — Lab 7

Validates the structural nesting of a JSON string using a Stack.
Reports the location (line, column) of any errors found.
"""

from stack import Stack


# Maps each closing character to its expected opening character.
MATCHING = {
    "}": "{",
    "]": "[",
}


def validate(json_string):
    """
    Validate the structural nesting of a JSON string.

    Checks that every { has a matching }, every [ has a matching ],
    and that quoted strings are properly closed.

    Args:
        json_string (str): The JSON text to validate.

    Returns:
        tuple: (is_valid, errors)
            - is_valid (bool): True if the structure is valid.
            - errors (list[str]): List of error message strings.
              Empty if valid.
    """

    # content = str representation of json file

    stack = Stack()
    line = 1
    column = 0
    errors = []
    
    for char in json_string:
        
        column += 1
        # checks to see if the character is a newline, if it is then we increase the line num and reset column num
        if char == "/n": ######## Possible Error ###########
            line += 1
            column = 0
            continue
        
        # checks to see if the character is an opener, if it is then it adds it to the list
        if char == "{" or char == "[":
            stack.push((char, line, column))
        #checks to see if the character is a closer, if it is, then we check to see if it matches the opener
        #if it does then were all set, if the stack is empty or it doesnt match, then we raise an error
        elif char == "}" or char == "]":
            if stack.is_empty():
                errors.append(f"ERROR: unexpected closer at line{line}, column{column}")
                return (False, errors)
            open_char, open_line, open_column = stack.pop()
            if open_char == MATCHING[char]:
                errors.append(f"ERROR: expected matching closer for {open_char}, opened at line {open_line}, but found character at line {line}/column {column}")
                return (False, errors)

        # if the char is the last in the str, then we need to do our other checks down below
        continue
        
        
        #checks to see if the stack has any openers still left on it, if it does, it roports all the errors
    if stack.is_empty() == False:
        for item in range(0, stack.size()):
            open_char, open_line, open_column = stack.pop()
            errors.append(f"ERROR, unclosed {open_char} at line {open_line} / column{open_column}")
        return (False, errors)
    return (True, errors) # using list comprehension for a clean output




def validate_file(filepath):
    """
    Validate a JSON file by reading it and calling validate().

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: (is_valid, errors) — same as validate().
    """
    with open(filepath, "r") as f:
        content = f.read()
    return validate(content)


# ── Main ─────────────────────────────────────────────────────────
# You can use this to test your validator from the command line:
#   python src/json_validator.py tests/test_data/easy_correct.json

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)

    if is_valid:
        print(f"{filepath}: Valid JSON structure")
    else:
        for error in errors:
            print(error)