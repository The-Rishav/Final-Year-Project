import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=6, sticky="nsew")
        self.display.focus_set()

        # Define buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('C', 1, 4), ('AC', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('(', 2, 4), (')', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('sin', 3, 4), ('cos', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3), ('tan', 4, 4), ('sqrt', 4, 5)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, font=('Arial', 15), padx=10, pady=10,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            current = self.display.get()[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, current)
        elif char == 'AC':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
