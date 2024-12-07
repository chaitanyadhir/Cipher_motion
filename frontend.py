import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests

API_URL = "http://127.0.0.1:8000/analyze"

def analyze_code():
    code = code_input.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Input Error", "Please enter some Python code to analyze.")
        return

    try:
        response = requests.post(API_URL, json={"code": code})
        if response.status_code == 200:
            result = response.json()
            bottlenecks_output.delete("1.0", tk.END)
            suggestions_output.delete("1.0", tk.END)
            bottlenecks_output.insert(tk.END, result.get("bottlenecks", "No bottlenecks identified."))
            suggestions_output.insert(tk.END, result.get("suggestions", "No suggestions available."))
        else:
            messagebox.showerror("API Error", f"Error {response.status_code}: {response.text}")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to the backend: {e}")

root = tk.Tk()
root.title("Python Code Analyzer")

tk.Label(root, text="Enter Python Code:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=("Courier", 10))
code_input.grid(row=1, column=0, padx=10, pady=5)

analyze_button = ttk.Button(root, text="Analyze Code", command=analyze_code)
analyze_button.grid(row=2, column=0, padx=10, pady=5)

tk.Label(root, text="Potential Bottlenecks:", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=5, sticky="w")
bottlenecks_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=7, font=("Courier", 10))
bottlenecks_output.grid(row=4, column=0, padx=10, pady=5)

tk.Label(root, text="Optimization Suggestions:", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=5, sticky="w")
suggestions_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=7, font=("Courier", 10))
suggestions_output.grid(row=6, column=0, padx=10, pady=5)

root.mainloop()
