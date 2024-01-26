
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Calculator")
        self.root.geometry("300x400")

        # Variable to store the input expression
        self.expression_var = tk.StringVar()

        # Entry widget to display the expression
        entry = tk.Entry(root, textvariable=self.expression_var, font=("Arial", 18), justify="right", bd=10)
        entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

        # Button layout with custom colors
        buttons = [
            ('7', 1, 0, "#4CAF50"), ('8', 1, 1, "#4CAF50"), ('9', 1, 2, "#4CAF50"), ('/', 1, 3, "#FF9800"),
            ('4', 2, 0, "#4CAF50"), ('5', 2, 1, "#4CAF50"), ('6', 2, 2, "#4CAF50"), ('*', 2, 3, "#FF9800"),
            ('1', 3, 0, "#4CAF50"), ('2', 3, 1, "#4CAF50"), ('3', 3, 2, "#4CAF50"), ('-', 3, 3, "#FF9800"),
            ('0', 4, 0, "#4CAF50"), ('.', 4, 1, "#4CAF50"), ('=', 4, 2, "#2196F3"), ('+', 4, 3, "#FF9800")
        ]

        # Create buttons and add them to the grid
        for (text, row, column, color) in buttons:
            btn = tk.Button(root, text=text, command=lambda t=text: self.on_button_click(t),
                            font=("Arial", 14), bg=color, fg="white")
            btn.grid(row=row, column=column, sticky="nsew", ipadx=10, ipady=10)
            root.grid_columnconfigure(column, weight=1)
            root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, text):
        current_expression = self.expression_var.get()

        if text == "=":
            try:
                result = eval(current_expression)
                self.expression_var.set(result)
            except Exception as e:
                self.expression_var.set("Error")
        else:
            new_expression = current_expression + text
            self.expression_var.set(new_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
