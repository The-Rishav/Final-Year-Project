import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management with Sales Prediction")
        self.master.geometry("1000x600")

        # Color scheme
        self.primary_color = "#4CAF50"
        self.secondary_color = "#FFC107"
        self.tertiary_color = "#2196F3"
        self.bg_color = "#f0f0f0"

        # Main Frame
        self.main_frame = tk.Frame(master, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        self.header_label = tk.Label(self.main_frame, text="Inventory Management with Sales Prediction", font=("Helvetica", 20, "bold"), bg=self.primary_color, fg="white", pady=10)
        self.header_label.pack(fill=tk.X)

        # File Selection Frame
        self.file_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.file_frame.pack(pady=20)

        self.file_label = tk.Label(self.file_frame, text="Select Excel/CSV file:", font=("Helvetica", 12), bg=self.bg_color)
        self.file_label.grid(row=0, column=0, padx=10, pady=10)

        self.file_button = tk.Button(self.file_frame, text="Browse", command=self.load_file, font=("Helvetica", 12), bg=self.primary_color, fg="white")
        self.file_button.grid(row=0, column=1, padx=10, pady=10)

        # Months Entry Frame
        self.months_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.months_frame.pack()

        self.months_label = tk.Label(self.months_frame, text="Enter number of months:", font=("Helvetica", 12), bg=self.bg_color)
        self.months_label.grid(row=0, column=0, padx=10, pady=10)

        self.months_entry = tk.Entry(self.months_frame, font=("Helvetica", 12))
        self.months_entry.grid(row=0, column=1, padx=10, pady=10)

        # Predict Button
        self.predict_button = tk.Button(self.main_frame, text="Predict Sales", command=self.predict, font=("Helvetica", 12), bg=self.secondary_color, fg="white", pady=10)
        self.predict_button.pack(pady=20)

        # Graph Frame
        self.graph_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        self.figure = plt.figure(figsize=(9, 4))
        self.bar_ax = self.figure.add_subplot(131)
        self.line_ax = self.figure.add_subplot(132)
        self.pie_ax = self.figure.add_subplot(133)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

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

        # Sample code for sales prediction using SVM
        # Implement your sales prediction algorithm here using self.data

        # Sample code to display a bar chart
        self.bar_ax.clear()
        self.bar_ax.bar(['Product A', 'Product B', 'Product C'], [100, 200, 150], color=self.primary_color)
        self.bar_ax.set_ylabel('Sales', fontsize=12)
        self.bar_ax.set_title('Sales Prediction (Bar Chart)', fontsize=14)

        # Sample code to display a line chart
        self.line_ax.clear()
        self.line_ax.plot(['Product A', 'Product B', 'Product C'], [100, 200, 150], color=self.secondary_color, marker='o')
        self.line_ax.set_ylabel('Sales', fontsize=12)
        self.line_ax.set_title('Sales Prediction (Line Chart)', fontsize=14)

        # Display pie chart for sales distribution
        pie_data = [30, 40, 30]  # Sample data
        labels = ['Category A', 'Category B', 'Category C']
        self.pie_ax.pie(pie_data, labels=labels, autopct='%1.1f%%', colors=[self.tertiary_color, self.secondary_color, self.primary_color])
        self.pie_ax.set_title('Sales Distribution (Pie Chart)', fontsize=14)

        self.canvas.draw()


def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
