import os
import tkinter as tk
from tkinter import filedialog

from utils import reconcile_csv_util


class ReconciliationApp:
    def __init__(self, master):
        self.master = master
        master.title("CSV Reconciliation Tool")
        master.geometry("500x300")  # Set the initial size of the window

        self.source_label = tk.Label(master, text="Select Source CSV:")
        self.source_label.pack()

        self.source_button = tk.Button(
            master, text="Browse", command=self.browse_source
        )
        self.source_button.pack()

        self.target_label = tk.Label(master, text="Select Target CSV:")
        self.target_label.pack()

        self.target_button = tk.Button(
            master, text="Browse", command=self.browse_target
        )
        self.target_button.pack()

        self.run_button = tk.Button(
            master, text="Run Reconciliation", command=self.run_reconciliation
        )
        self.run_button.pack()

        self.source_path = ""
        self.target_path = ""

    def browse_source(self):
        self.source_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )
        print(f"Source CSV: {self.source_path}")

    def browse_target(self):
        self.target_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )
        print(f"Target CSV: {self.target_path}")

    def run_reconciliation(self):
        if not self.source_path or not self.target_path:
            print("Please select both source and target CSV files.")
            return

        output_path = reconcile_csv_util(self.source_path, self.target_path)
        print(f"Reconciliation completed. Output saved to: {output_path}")
        self.show_result(output_path)

    def show_result(self, output_path):
        result_window = tk.Toplevel(self.master)
        result_window.title("Reconciliation Result")

        result_label = tk.Label(
            result_window, text=f"Reconciliation Result\nOutput saved to: {output_path}"
        )
        result_label.pack()

        view_button = tk.Button(
            result_window,
            text="View Result",
            command=lambda: self.view_result(output_path),
        )
        view_button.pack()

    def view_result(self, output_path):
        if os.path.exists(output_path):
            os.system(
                f"open {output_path}"
            )  # Opens the file with the default application
        else:
            print("Result file not found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ReconciliationApp(root)
    root.mainloop()
