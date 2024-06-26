# Nikola Language Interpreter in Python

class NikolaInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.strip().split('\n')
        for line in lines:
            self.parse_line(line.strip())

    def parse_line(self, line):
        if line.startswith('print '):
            value = self.evaluate_expression(line[6:])
            print(value)
        elif '=' in line:
            var_name, expression = line.split('=')
            self.variables[var_name.strip()] = self.evaluate_expression(expression.strip())

    def evaluate_expression(self, expression):
        # Simple arithmetic operations
        try:
            return eval(expression, {}, self.variables)
        except NameError as e:
            print(f"Undefined variable: {e}")
        except Exception as e:
            print(f"Error: {e}")

# Example Nikola code
nikola_code = """
x = 10
y = 20
print x + y
"""

interpreter = NikolaInterpreter()
interpreter.run(nikola_code)
