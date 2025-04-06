# Custom-Instruction
Design a custom instruction for a given equation in compiler.


# Custom Instruction Generator

This is a Streamlit web application that reads code from an uploaded `.txt` or `.py` file and generates custom low-level assembly-like instructions based on control structures and assignments. The custom instruction set includes operations like `LOAD`, `ADD`, `SUB`, `GOTO`, `IF`, `LABEL`, etc.

---

## Live Demo

Deployed Website: **[Add your deployed website link here]**

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
   git clone https://github.com/your-username/custom-instruction-generator.git
   cd custom-instruction-generator
   ```

2. Install dependencies
   ```bash
   pip install streamlit
   ```

3. Run the app
   ```bash
   streamlit run your_script_name.py
   ```

4. Open `http://localhost:8501` in your browser to use the app.

---

## Example Input

```python
a = 5
b = 10
c = a + b

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
ADD R3, R1, R2
STORE c, R3
IF a < b GOTO L1
GOTO L2
LABEL L1:
ADD R4, R3, R5
STORE c, R4
GOTO L3
LABEL L2:
SUB R4, R3, R5
STORE c, R4
LABEL L3:
LABEL L4:
IF NOT c < 20 GOTO L5
ADD R6, R4, R7
STORE c, R6
GOTO L4
LABEL L5:
```

---

## Tech Stack

- Python
- Streamlit

---

## Future Enhancements

- Syntax highlighting for the output.
- Option to download output as a `.asm` or `.txt` file.
- Real-time editing support inside the app.


