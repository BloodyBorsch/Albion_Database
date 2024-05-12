from Data_Controller import DB


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

def add_command(db: DB):
    db.insert_data(product_text.get(), price_text.get(), comment_text.get()) 
    