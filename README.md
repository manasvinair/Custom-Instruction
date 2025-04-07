# Custom-Instruction
Design a custom instruction for a given equation in compiler.

## Submitted by : Manasvi Nair (23115056)

# Custom Instruction Generator

This is a Streamlit web application that reads code from an uploaded `.txt` or `.py` file and generates custom low-level assembly-like instructions based on control structures and assignments. The custom instruction set includes operations like `LOAD`, `ADD`, `SUB`, `GOTO`, `IF`, `LABEL`, etc.

---

## Live Demo

Deployed Website: **(https://custom-instruction-23115056.streamlit.app/)**

---

## Features

- Upload Python-like code with assignments, `if-else` statements, and `while` loops.
- Automatically generate a corresponding sequence of custom instructions.
- View the instructions directly in the browser.
- Save the output to a downloadable `output.txt` file.

---

## How to Run Locally

1. Clone the repository
   ```bash
   git clone https://github.com/manasvinair/Custom-Instruction.git
   cd Custom-Instruction
   ```

2. Install dependencies
   ```bash
   pip install streamlit
   ```

3. Run the app
   ```bash
   streamlit run custominstruction.py
   ```

4. Open `http://localhost:8501` in your browser to use the app.

---

## Example Input

```python
a = 5
b = 10
c = 9
d = a + b * c

if a < b:
    c = c + 1
else:
    c = c - 1

while c < 20:
    c = c + 2

```

---

## Sample Output

```assembly
LOAD R1, 5
STORE a, R1
LOAD R2, 10
STORE b, R2
LOAD R3, 9
STORE c, R3
MANA a, b, c
STORE d, a
IF a < b GOTO L1
LOAD R4, 1
ADD R5, R3, R4
STORE c, R5
GOTO L2
LABEL L1:
LOAD R6, 1
SUB R7, R5, R6
STORE c, R7
LABEL L2:
LABEL L3:
IF NOT c < 20 GOTO L4
LOAD R8, 2
ADD R9, R7, R8
STORE c, R9
GOTO L3
LABEL L4:

```

---

## Tech Stack

- Python
- Streamlit


