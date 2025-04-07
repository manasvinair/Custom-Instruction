import streamlit as st
import os

class InstructionGenerator:
    def __init__(self):
        self.instructions = []
        self.register_count = 1
        self.label_count = 1
        self.variables = {}
        self.lines = []

    # Lexical Analysis
    def tokenize(self, code):
        return code.strip().split('\n')

    def get_register(self):
        reg = f"R{self.register_count}"
        self.register_count += 1
        return reg

    def get_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    # Syntax + Semantic Analysis + Intermediate Code Generation
    def handle_assignment(self, line):
        var, expr = line.split('=')
        var = var.strip()
        expr = expr.strip()

        # Check for a + b * c pattern
        if '+' in expr and '*' in expr:
        # Handle a + b * c as mana a, b, c
        # Basic parsing assuming format: a + b * c
            parts = expr.split('+')
            a = parts[0].strip()
            b_mul_c = parts[1].strip()
            if '*' in b_mul_c:
                b, c = b_mul_c.split('*')
                b = b.strip()
                c = c.strip()
                self.instructions.append(f"MANA {a}, {b}, {c}")
                self.instructions.append(f"STORE {var}, {a}")  # Assuming result is stored in a
                return

        # Standard expressions
        if '+' in expr:
            op1, op2 = expr.split('+')
            r1 = self.load_operand(op1.strip())
            r2 = self.load_operand(op2.strip())
            r3 = self.get_register()
            self.instructions.append(f"ADD {r3}, {r1}, {r2}")
        elif '-' in expr:
            op1, op2 = expr.split('-')
            r1 = self.load_operand(op1.strip())
            r2 = self.load_operand(op2.strip())
            r3 = self.get_register()
            self.instructions.append(f"SUB {r3}, {r1}, {r2}")
        elif '*' in expr:
            op1, op2 = expr.split('*')
            r1 = self.load_operand(op1.strip())
            r2 = self.load_operand(op2.strip())
            r3 = self.get_register()
            self.instructions.append(f"MUL {r3}, {r1}, {r2}")
        elif '/' in expr:
            op1, op2 = expr.split('/')
            r1 = self.load_operand(op1.strip())
            r2 = self.load_operand(op2.strip())
            r3 = self.get_register()
            self.instructions.append(f"DIV {r3}, {r1}, {r2}")
        else:
            r3 = self.load_operand(expr.strip())
        self.instructions.append(f"STORE {var}, {r3}")
        self.variables[var] = r3


    def load_operand(self, operand):
        if operand.isdigit():
            r = self.get_register()
            self.instructions.append(f"LOAD {r}, {operand}")
            return r
        elif operand in self.variables:
            return self.variables[operand]
        else:
            r = self.get_register()
            self.instructions.append(f"LOAD {r}, {operand}")
            self.variables[operand] = r
            return r

    # Handling if-else
    def handle_if_else(self, lines, i):
        condition = lines[i][3:-1].strip()
        label1 = self.get_label()
        label2 = self.get_label()

        self.instructions.append(f"IF {condition} GOTO {label1}")
        i += 1
        while i < len(lines) and self.is_indented(lines[i]):
            i = self.handle_line(lines[i].strip(), i)
        self.instructions.append(f"GOTO {label2}")
        self.instructions.append(f"LABEL {label1}:")

        if i < len(lines) and lines[i].strip() == "else:":
            i += 1
            while i < len(lines) and self.is_indented(lines[i]):
                i = self.handle_line(lines[i].strip(), i)

        self.instructions.append(f"LABEL {label2}:")
        return i

    # Handling loops
    def handle_while_loop(self, lines, i):
        condition = lines[i][6:-1].strip()
        start_label = self.get_label()
        end_label = self.get_label()

        self.instructions.append(f"LABEL {start_label}:")
        self.instructions.append(f"IF NOT {condition} GOTO {end_label}")
        i += 1
        while i < len(lines) and self.is_indented(lines[i]):
            i = self.handle_line(lines[i].strip(), i)
        self.instructions.append(f"GOTO {start_label}")
        self.instructions.append(f"LABEL {end_label}:")
        return i

    # Semantic Analysis + IR Generation
    def handle_line(self, line, i):
        if line.startswith("if "):
            return self.handle_if_else(self.lines, i)
        elif line.startswith("while "):
            return self.handle_while_loop(self.lines, i)
        elif "=" in line:
            self.handle_assignment(line)
            return i + 1
        return i + 1

    def is_indented(self, line):
        return line.startswith("    ") or line.startswith("\t")

    # Code Generation Phase
    def generate(self, code):
        self.lines = self.tokenize(code)
        i = 0
        while i < len(self.lines):
            line = self.lines[i].strip()
            if line == "":
                i += 1
                continue
            if line.startswith("if "):
                i = self.handle_if_else(self.lines, i)
            elif line.startswith("while "):
                i = self.handle_while_loop(self.lines, i)
            else:
                i = self.handle_line(line, i)
        return self.instructions


# Driver Code
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        code = f.read()

    gen = InstructionGenerator()
    instructions = gen.generate(code)

    with open("output.txt", "w") as f:
        for instr in instructions:
            f.write(instr + "\n")

    print("Custom instructions written to:", os.path.abspath("output.txt"))
    
    

#streamlit UI
st.title("Custom Instruction Generator")

uploaded_file = st.file_uploader("Upload your input .txt or .py file", type=["txt", "py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    st.subheader("Input Code")
    st.code(code, language="python")

    generator = InstructionGenerator()
    instructions = generator.generate(code)

    st.subheader("Generated Custom Instructions")
    for instr in instructions:
        st.text(instr)