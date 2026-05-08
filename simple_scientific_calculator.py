import tkinter as tk
from tkinter import messagebox
import math

class BasicCalculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

    def derivative_at_point(self, val):
        h = 0.000001
        f = lambda x: x ** 2
        return (f(val + h) - f(val)) / h


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemini Engineering Calc")
        self.calc_engine = EngineeringCalculator()

        self.result_var = tk.StringVar(value="0")
        self.create_widgets()

    def create_widgets(self):
        # Display Screen
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), borderwidth=5, relief="flat",
                         justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Button Definitions (Text, Row, Col, Command)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('√n', 5, 2), ('d/dx x²', 5, 3),
            ('=', 6, 0, 4)  # Span 4 columns
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1

            action = lambda x=text: self.on_click(x)
            tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14),
                      command=action).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def on_click(self, char):
        current_val = self.result_var.get()

        try:
            if char == 'C':
                self.result_var.set("0")
            elif char == '=':
                # Basic Expression Parsing
                res = eval(current_val)
                self.result_var.set(res)
                self.ask_try_again()
            elif char == 'sin':
                self.result_var.set(self.calc_engine.sine(float(current_val)))
            elif char == 'cos':
                self.result_var.set(self.calc_engine.cosine(float(current_val)))
            elif char == '√n':
                # Custom prompt for nth root
                n = 2  # Default to square root, could be expanded
                self.result_var.set(self.calc_engine.nth_root(float(current_val), n))
            elif char == 'd/dx x²':
                self.result_var.set(self.calc_engine.derivative_at_point(float(current_val)))
            else:
                if current_val == "0":
                    self.result_var.set(char)
                else:
                    self.result_var.set(current_val + char)