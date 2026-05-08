import tkinter as tk
from tkinter import messagebox
import math

# --- OOP: Base Class (Encapsulation) ---
class BasicCalculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b