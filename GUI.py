import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class MultiToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Multi-Tool Dashboard")
        self.root.geometry("550x500")
        
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
            
        style.configure("TFrame", background="#f4f4f9")
        style.configure("TLabel", background="#f4f4f9", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#333333")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.user_score = 0
        self.comp_score = 0

        self.create_todo_tab()
        self.create_calc_tab()
        self.create_password_tab()
        self.create_rps_tab()
        self.create_contact_tab()

    # Tab 1: To-Do List
    def create_todo_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📝 To-Do")

        ttk.Label(tab, text="Task Manager", style="Header.TLabel").pack(pady=10)

        input_frame = ttk.Frame(tab)
        input_frame.pack(pady=5)

        self.task_entry = ttk.Entry(input_frame, width=30, font=("Segoe UI", 11))
        self.task_entry.grid(row=0, column=0, padx=5)
        
        ttk.Button(input_frame, text="Add Task", command=self.add_task).grid(row=0, column=1)

        self.task_listbox = tk.Listbox(tab, width=45, height=10, font=("Segoe UI", 11), selectbackground="#4a90e2")
        self.task_listbox.pack(pady=10)
        
        self.task_listbox.bind("<<ListboxSelect>>", self.load_task_to_entry)

        btn_frame = ttk.Frame(tab)
        btn_frame.pack()
        
        ttk.Button(btn_frame, text="Update Selected", command=self.update_task).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_task).grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def load_task_to_entry(self, event):
        selection = self.task_listbox.curselection()
        if selection:
            task = self.task_listbox.get(selection[0])
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task)

    def update_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get().strip()
            
            if updated_task:
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, updated_task)
                self.task_entry.delete(0, tk.END)
                self.task_listbox.select_set(selected)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    # Tab 2: Calculator
    def create_calc_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🧮 Calculator")

        ttk.Label(tab, text="Quick Calculator", style="Header.TLabel").pack(pady=20)

        calc_frame = ttk.Frame(tab)
        calc_frame.pack(pady=10)

        self.num1_entry = ttk.Entry(calc_frame, width=10, font=("Segoe UI", 12))
        self.num1_entry.grid(row=0, column=0, padx=5)

        self.op_var = tk.StringVar(value="+")
        op_menu = ttk.Combobox(calc_frame, textvariable=self.op_var, values=["+", "-", "*", "/"], width=3, state="readonly", font=("Segoe UI", 12))
        op_menu.grid(row=0, column=1, padx=5)

        self.num2_entry = ttk.Entry(calc_frame, width=10, font=("Segoe UI", 12))
        self.num2_entry.grid(row=0, column=2, padx=5)

        ttk.Button(tab, text="Calculate", command=self.calculate).pack(pady=15)
        
        self.calc_result = ttk.Label(tab, text="Result: ", font=("Segoe UI", 14, "bold"), foreground="#007acc")
        self.calc_result.pack()

    def calculate(self):
        try:
            n1 = float(self.num1_entry.get())
            n2 = float(self.num2_entry.get())
            op = self.op_var.get()

            if op == "+": res = n1 + n2
            elif op == "-": res = n1 - n2
            elif op == "*": res = n1 * n2
            elif op == "/":
                if n2 == 0:
                    self.calc_result.config(text="Error: Divide by zero")
                    return
                res = n1 / n2
                
            if res.is_integer(): 
                res = int(res)
            self.calc_result.config(text=f"Result: {res}")
        except ValueError:
            self.calc_result.config(text="Error: Invalid Numbers")

    # Tab 3: Password Generator
    def create_password_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔑 Passwords")

        ttk.Label(tab, text="Secure Password Generator", style="Header.TLabel").pack(pady=20)

        ttk.Label(tab, text="Select Length:").pack()
        self.len_var = tk.IntVar(value=12)
        
        length_slider = ttk.Scale(tab, from_=4, to_=32, orient="horizontal", variable=self.len_var, command=lambda e: self.len_label.config(text=f"{self.len_var.get()} chars"))
        length_slider.pack(pady=5, fill="x", padx=100)
        
        self.len_label = ttk.Label(tab, text="12 chars")
        self.len_label.pack()

        ttk.Button(tab, text="Generate Password", command=self.generate_password).pack(pady=20)

        self.pass_entry = ttk.Entry(tab, font=("Courier", 14), justify="center")
        self.pass_entry.pack(fill="x", padx=50, pady=10)

    def generate_password(self):
        length = self.len_var.get()
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(chars, k=length))
        
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, password)

    # Tab 4: Rock-Paper-Scissors
    def create_rps_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🎮 R-P-S")

        ttk.Label(tab, text="Rock, Paper, Scissors", style="Header.TLabel").pack(pady=15)
        
        self.score_label = ttk.Label(tab, text="You: 0  |  Computer: 0", font=("Segoe UI", 12, "bold"))
        self.score_label.pack(pady=5)

        self.rps_result_label = ttk.Label(tab, text="Make your move!", font=("Segoe UI", 12))
        self.rps_result_label.pack(pady=15)

        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="🪨 Rock", command=lambda: self.play_rps("rock")).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="📄 Paper", command=lambda: self.play_rps("paper")).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="✂️ Scissors", command=lambda: self.play_rps("scissors")).grid(row=0, column=2, padx=10)

    def play_rps(self, user_choice):
        options = ["rock", "paper", "scissors"]
        comp_choice = random.choice(options)
        
        win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        if user_choice == comp_choice:
            result = f"Both chose {user_choice}. It's a Tie!"
        elif win_conditions[user_choice] == comp_choice:
            result = f"{user_choice.capitalize()} beats {comp_choice}. You Win!"
            self.user_score += 1
        else:
            result = f"{comp_choice.capitalize()} beats {user_choice}. You Lose!"
            self.comp_score += 1

        self.rps_result_label.config(text=result)
        self.score_label.config(text=f"You: {self.user_score}  |  Computer: {self.comp_score}")

    # Tab 5: Contact Book
    def create_contact_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📇 Contacts")

        columns = ("Name", "Phone")
        self.tree = ttk.Treeview(tab, columns=columns, show="headings", height=5)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.pack(fill="x", padx=20, pady=10)
        
        self.tree.bind("<<TreeviewSelect>>", self.load_contact_to_entry)

        input_frame = ttk.Frame(tab)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.contact_name = ttk.Entry(input_frame)
        self.contact_name.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(input_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.contact_phone = ttk.Entry(input_frame)
        self.contact_phone.grid(row=1, column=1, padx=5, pady=2)

        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=5)
        
        ttk.Button(btn_frame, text="Add", command=self.add_contact).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_contact).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_contact).grid(row=0, column=2, padx=5)

    def add_contact(self):
        name = self.contact_name.get().strip()
        phone = self.contact_phone.get().strip()
        
        if name and phone:
            self.tree.insert("", tk.END, values=(name, phone))
            self.contact_name.delete(0, tk.END)
            self.contact_phone.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both Name and Phone.")

    def delete_contact(self):
        selected = self.tree.selection()
        if selected:
            for item in selected:
                self.tree.delete(item)
            self.contact_name.delete(0, tk.END)
            self.contact_phone.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def load_contact_to_entry(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.contact_name.delete(0, tk.END)
            self.contact_name.insert(0, values[0])
            self.contact_phone.delete(0, tk.END)
            self.contact_phone.insert(0, values[1])

    def update_contact(self):
        selected = self.tree.selection()
        if selected:
            name = self.contact_name.get().strip()
            phone = self.contact_phone.get().strip()
            
            if name and phone:
                self.tree.item(selected[0], values=(name, phone))
                self.contact_name.delete(0, tk.END)
                self.contact_phone.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter both Name and Phone to update.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiToolApp(root)
    root.mainloop()