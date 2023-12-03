import tkinter as tk
from tkinter import ttk, messagebox
from data import fetch_data
from HashTable import HashTable
from Btree import BTree
import time
import pandas as pd
class CrimeDataApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Data Analysis")
        self.root.geometry("600x400")  # Set the size of the window (width x height)

        # Initialize hash table and B-tree
        self.hash_table = HashTable()
        self.b_tree = BTree()
        # Add a variable to track the selected search method
        self.search_method_var = tk.StringVar(value="hash_table")
        self.sort_order = {}
        # Create main menu buttons
        self.create_main_menu()


    def create_main_menu(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Add radio buttons for selecting the search method
        radio1 = tk.Radiobutton(main_frame, text="Hash Table", variable=self.search_method_var, value="hash_table")
        radio1.pack()
        radio2 = tk.Radiobutton(main_frame, text="B-Tree", variable=self.search_method_var, value="b_tree")
        radio2.pack()

        btn_crime_type = tk.Button(main_frame, text="Search by Crime Type", command=self.open_crime_type_search)
        btn_crime_type.pack(fill='x', padx=5, pady=5)


    def fetch_and_process_data(self):
        data = fetch_data()
        for index, row in data.iterrows():
            key = row['district']  # Using 'district' as a key
            self.hash_table.insert(key, row.to_dict())
            self.b_tree.insert(key, row.to_dict())




    # Define other methods for sub-menus, data display, etc.

    def open_crime_type_search(self):
        crime_type_window = tk.Toplevel(self.root)
        crime_type_window.title("Search by Crime Type")
        crime_type_window.geometry("400x200")  # Adjust size as needed

        frame = tk.Frame(crime_type_window)
        frame.pack(padx=10, pady=10)

        label = tk.Label(frame, text="Enter Crime Type:")
        label.pack()
        
        entry = tk.Entry(frame)
        entry.pack()

        search_button = tk.Button(frame, text="Search", command=lambda: self.search_crime_type(entry.get()))
        search_button.pack(pady=5)


    def search_crime_type(self, crime_type):
        search_method = self.search_method_var.get()
        if search_method == "hash_table":
            self.search_crime_type_hash_table(crime_type)
        elif search_method == "b_tree":
            self.search_crime_type_b_tree(crime_type)
    
    def search_crime_type_hash_table(self, crime_type):
        start_time_ns = time.perf_counter_ns()  # Start timing in nanoseconds
        results = []
        for bucket in self.hash_table.table:
            for key, record in bucket:
                if record['primary_type'].lower() == crime_type.lower():
                    results.append(record)
        end_time_ns = time.perf_counter_ns()  # End timing in nanoseconds
        search_duration_ns = end_time_ns - start_time_ns  # Calculate duration in nanoseconds

        print(f"Hash table search time: {search_duration_ns} ns")

        if results:
            results_df = pd.DataFrame(results)
            self.display_data(results_df)
        else:
            messagebox.showinfo("No results", "No matching records found.")

    def search_crime_type_b_tree(self, crime_type):
        start_time_ns = time.perf_counter_ns()  # Start timing in nanoseconds
        # Implement B-tree search logic here
        # Make sure to populate the 'results' list with the search results
        end_time_ns = time.perf_counter_ns()  # End timing in nanoseconds
        search_duration_ns = end_time_ns - start_time_ns  # Calculate duration in nanoseconds

        print(f"B-tree search time: {search_duration_ns} ns")

        if results:
            results_df = pd.DataFrame(results)
            self.display_data(results_df)
        else:
            messagebox.showinfo("No results", "No matching records found.")

        
    def display_data(self, data):
        display_window = tk.Toplevel(self.root)
        display_window.title("Search Results")
        display_window.geometry("800x600")

        tree_frame = tk.Frame(display_window)
        tree_frame.pack(fill='both', expand=True)

        tree = ttk.Treeview(tree_frame, columns=("date", "district", "primary_type", "description"), show='headings')


        for col in tree["columns"]:
            self.sort_order[col] = True  # Initialize sorting order as ascending for each column
            tree.heading(col, text=col.title(), command=lambda _col=col: self.sort_column(tree, _col))
            
        tree.column("date", width=150)  # Adjust width as needed
        tree.heading("date", text="Date")



        # Correct way to iterate over rows in a DataFrame
        for index, row in data.iterrows():
            # Convert date to string if necessary
            date_str = row["date"].strftime("%Y-%m-%d %H:%M:%S") if pd.notnull(row["date"]) else ""
            tree.insert("", "end", values=(date_str, row["district"], row["primary_type"], row["description"]))

        tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
    
    def sort_column(self, tree, col):
        start_time = time.perf_counter_ns()  # Start timing in nanoseconds

        reverse = self.sort_order[col]
        data_list = [(tree.set(k, col), k) for k in tree.get_children('')]
        data_list.sort(reverse=reverse)

        # Rearrange items in sorted positions
        for index, (val, k) in enumerate(data_list):
            tree.move(k, '', index)

        # Update column header with sorting arrow
        arrow = '↓' if reverse else '↑'
        for c in tree["columns"]:
            if c == col:
                tree.heading(c, text=f'{c.title()} {arrow}', command=lambda _col=c: self.sort_column(tree, _col))
            else:
                tree.heading(c, text=c.title(), command=lambda _col=c: self.sort_column(tree, _col))

        # Reverse the sort order for the next time
        self.sort_order[col] = not reverse

        end_time = time.perf_counter_ns()  # End timing in nanoseconds
        time_diff_ns = end_time - start_time
        print(f"Sorting time for column '{col}': {time_diff_ns} nanoseconds")  # Displaying the time taken in nanoseconds






    # Implement similar methods for other search options

def main():
    root = tk.Tk()
    app = CrimeDataApp(root)
    app.fetch_and_process_data()  # Load data into structures
    root.mainloop()


if __name__ == "__main__":
    main()
