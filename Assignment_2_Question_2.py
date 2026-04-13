# Group Name: [DAN/EXT 73]

# Group Member:
# Patrick Burzynski - [399755]

# Question 2
"""This program reads mathematical expressions from a text file, evaluates them using recursive descent parsing,
and writes the results to an output file."""

# Tokenize
def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        char = expr[i]
        
        # build multi-digit numbers
        if char.isdigit():
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(("NUM", num))
            continue
        
        #operators
        elif char in "+-*/":
            tokens.append(("OP", char))
            
        #brackets
        elif char == "(":
            tokens.append(("LPAREN", "("))     
        elif char == ")":
            tokens.append(("RPAREN", ")"))
        i += 1
    tokens.append(("END", ""))
    return tokens

def evaluate_file(input_path):
    with open(input_path, "r") as file:
        lines = file.readlines()
      
