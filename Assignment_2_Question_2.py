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

#Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0      
    # return current token
    def current(self):
        return self.tokens[self.pos]    
    # move to next token
    def eat(self):
        self.pos += 1

    # handles + and -
    def expression(self):
        value, tree = self.term()
        while self.current()[1] in ["+", "-"]:
            op = self.current()[1]
            self.eat()
            rhs, rhs_tree = self.term()
            if op == "+":
                value += rhs
            else:
                value -= rhs
            tree = f"({op} {tree} {rhs_tree})"
        return value, tree

    # handles * and /
    def term(self):
        value, tree = self.factor()
        while self.current()[1] in ["*", "/"]:
            op = self.current()[1]
            self.eat()
            rhs, rhs_tree = self.factor()
            if op == "/":
                if rhs == 0:
                    return None, "ERROR"
                value /= rhs
            else:
                value *= rhs
            tree = f"({op} {tree} {rhs_tree})"
        return value, tree

    #handles numbers, brackets and unary minus
    def factor(self):
        token_type, token_value = self.current()
        
        # unary minus
        if token_type == "OP" and token_value == "-":
            self.eat()
            value, tree = self.factor()
            return -value, f"(neg {tree})"
        
        # brackets
        if token_type == "LPAREN":
            self.eat()
            value, tree = self.expression()
            self.eat()
            return value, f"({tree})"
        
        # number
        if token_type == "NUM":
            self.eat()
            return float(token_value), token_value
        return None, "ERROR"

def evaluate_file(input_path):
    with open(input_path, "r") as file:
        lines = file.readlines()
      
