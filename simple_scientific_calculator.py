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