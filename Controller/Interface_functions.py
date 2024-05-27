from tkinter import *
from tkinter import ttk
from Data_Controller import Data_Base


def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print(
        "   " * depth
        + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}"
    )
    for child in widget.winfo_children():
        print_info(child, depth + 1)

def clear_table():
    pass
