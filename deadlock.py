import tkinter as tk
from tkinter import ttk, messagebox

class RoundedButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = ttk.Style()
        self.style.configure("Rounded.TButton", padding=10, relief="flat", background="#4CAF50", foreground="white", font=("Helvetica", 12, "bold"))
        self.configure(style="Rounded.TButton")

class RoundedEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = ttk.Style()
        self.style.configure("Rounded.TEntry", padding=10, relief="flat", background="white", foreground="black", font=("Helvetica", 12))
        self.configure(style="Rounded.TEntry")

class DeadlockDetection:
    def __init__(self, master):
        self.master = master
        self.master.title("Deadlock Detection and Prevention")
        self.master.configure(bg="white")  # Set background color to white
        self.master.geometry("1280x768")  # Set window size
        
        # Main Frame
        self.main_frame = ttk.Frame(master, padding=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Title Label
        self.title_label = ttk.Label(self.main_frame, text="Deadlock Detection and Prevention", font=("Helvetica", 18, "bold"), background="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Processes and Resources Input
        self.processes_label = ttk.Label(self.main_frame, text="Number of Processes:", background="white")
        self.processes_label.grid(row=1, column=0, sticky=tk.E)
        self.processes_entry = RoundedEntry(self.main_frame, width=5)
        self.processes_entry.grid(row=1, column=1, padx=10)

        self.resources_label = ttk.Label(self.main_frame, text="Number of Resources:", background="white")
        self.resources_label.grid(row=2, column=0, sticky=tk.E)
        self.resources_entry = RoundedEntry(self.main_frame, width=5)
        self.resources_entry.grid(row=2, column=1, padx=10)

        self.next_button = RoundedButton(self.main_frame, text="Next", command=self.next_step)
        self.next_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.allocation_matrix = []
        self.request_matrix = []
        self.available_vector = []

    def next_step(self):
        try:
            self.num_processes = int(self.processes_entry.get())
            self.num_resources = int(self.resources_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for processes and resources.")
            return
        
        self.input_allocation_request()

    def input_allocation_request(self):
        self.clear_window()
        
        tk.Label(self.main_frame, text="Enter Allocation Matrix", font=("Helvetica", 14), background="white").grid(row=0, column=0, columnspan=2, pady=(0, 10))
        self.allocation_matrix = self.create_matrix_input(self.num_processes, self.num_resources, 1)
        
        tk.Label(self.main_frame, text="Enter Request Matrix", font=("Helvetica", 14), background="white").grid(row=self.num_processes + 1, column=0, columnspan=2, pady=(20, 10))
        self.request_matrix = self.create_matrix_input(self.num_processes, self.num_resources, self.num_processes + 2)
        
        tk.Label(self.main_frame, text="Enter Available Vector", font=("Helvetica", 14), background="white").grid(row=(self.num_processes * 2) + 2, column=0, columnspan=2, pady=(20, 10))
        self.available_vector = self.create_vector_input(self.num_resources, (self.num_processes * 2) + 3)
        
        self.detect_button = RoundedButton(self.main_frame, text="Detect Deadlock", command=self.detect_deadlock)
        self.detect_button.grid(row=(self.num_processes * 2) + 4, column=0, columnspan=2, pady=20)

    def create_matrix_input(self, rows, cols, start_row):
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                entry = RoundedEntry(self.main_frame, width=5)
                entry.grid(row=start_row + i, column=j, padx=5)
                row.append(entry)
            matrix.append(row)
        return matrix
    
    def create_vector_input(self, size, start_row):
        vector = []
        for i in range(size):
            entry = RoundedEntry(self.main_frame, width=5)
            entry.grid(row=start_row, column=i, padx=5)
            vector.append(entry)
        return vector

    def get_matrix(self, matrix):
        result = []
        for row in matrix:
            result.append([int(entry.get()) for entry in row])
        return result

    def get_vector(self, vector):
        return [int(entry.get()) for entry in vector]

    def detect_deadlock(self):
        try:
            allocation = self.get_matrix(self.allocation_matrix)
            request = self.get_matrix(self.request_matrix)
            available = self.get_vector(self.available_vector)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for matrix values.")
            return
        
        work = available[:]
        finish = [False] * self.num_processes
        safe_sequence = []

        for _ in range(self.num_processes):
            process_found = False
            for i in range(self.num_processes):
                if not finish[i]:
                    if all(request[i][j] <= work[j] for j in range(self.num_resources)):
                        work = [work[j] + allocation[i][j] for j in range(self.num_resources)]
                        finish[i] = True
                        safe_sequence.append(i)
                        process_found = True
                        break

            if not process_found:
                break

        if all(finish):
            messagebox.showinfo("Result", f"No Deadlock Detected! Safe Sequence: {safe_sequence}")
        else:
            messagebox.showerror("Result", "Deadlock Detected!")

    def clear_window(self):
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

def main():
    root = tk.Tk()
    app = DeadlockDetection(root)
    root.mainloop()

if __name__ == "__main__":
    main()
