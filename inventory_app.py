import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management with Sales Prediction")
        self.master.geometry("600x400")

        self.file_label = tk.Label(master, text="Select Excel/CSV file:")
        self.file_label.pack()

        self.file_button = tk.Button(master, text="Browse", command=self.load_file)
        self.file_button.pack()

        self.months_label = tk.Label(master, text="Enter number of months:")
        self.months_label.pack()

        self.months_entry = tk.Entry(master)
        self.months_entry.pack()

        self.predict_button = tk.Button(master, text="Predict Sales", command=self.predict)
        self.predict_button.pack()

        self.figure = plt.figure(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.get_tk_widget().pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)

    def predict(self):
        try:
            months = int(self.months_entry.get())
            if months <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of months.")
            return

        # Implement your sales prediction algorithm here using self.data

        # Sample code to display a bar chart (replace with your own data)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(['Product A', 'Product B', 'Product C'], [100, 200, 150])
        ax.set_ylabel('Sales')
        ax.set_title('Sales Prediction')
        self.canvas.draw()


def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
