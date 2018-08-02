# Import Tkinter
from tkinter import *

# Define ticket class
class Ticket:
    def __init__(self, time, capacity, cost):
        self._time = time
        self._capacity = int(capacity)
        self._sold = 0
        self._cost = float(cost)
    
Ticket("10am", 150, 5)
Ticket("3pm", 150, 5)
Ticket("8pm", 250, 12)
