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

        # Heading for choosing the data structure
        data_structure_label = tk.Label(main_frame, text="Choose the data structure to search by")
        data_structure_label.pack()

        # Add radio buttons for selecting the search method
        radio1 = tk.Radiobutton(main_frame, text="Hash Table", variable=self.search_method_var, value="hash_table")
        radio1.pack()
        radio2 = tk.Radiobutton(main_frame, text="B-Tree", variable=self.search_method_var, value="b_tree")
        radio2.pack()

        crime_types = self.fetch_crime_types()

        #Drop down box for crime types
        crime_type_label = tk.Label(main_frame, text="Select Crime Type:")
        crime_type_label.pack()

        self.selected_crime_type = tk.StringVar()
        crime_type_dropdown = ttk.Combobox(main_frame, textvariable=self.selected_crime_type, values=crime_types)
        crime_type_dropdown.pack()
        
        # Add a label and entry for date input
        date_label = tk.Label(main_frame, text="Enter Date (YYYY-MM-DD):")
        date_label.pack()

        self.date_entry = tk.Entry(main_frame)
        self.date_entry.pack()


        search_button = tk.Button(main_frame, text="Search", command=self.search_selected_crime_type)
        search_button.pack(fill='x', padx=5, pady=5)

    def fetch_crime_types(self):
        data = fetch_data()  # Fetch data
        crime_types = data['primary_type'].unique().tolist()  # Extract unique crime types
        crime_types.sort()
        return crime_types 

    def fetch_and_process_data(self):
        data = fetch_data()
        #timer
        # Start timing for hash table insertion
        start_time_ht = time.perf_counter_ns()
        for index, row in data.iterrows():
            key = row['primary_type']  # Using 'primary_type' as a key
            self.hash_table.insert(key.lower(), row.to_dict())
        end_time_ht = time.perf_counter_ns()
        duration_ht = end_time_ht - start_time_ht

        # Start timing for B-tree insertion
        start_time_bt = time.perf_counter_ns()
        for index, row in data.iterrows():
            key = row['primary_type']  # Using 'primary_type' as a key
            self.b_tree.insert(key.lower(), row.to_dict())
        end_time_bt = time.perf_counter_ns()
        duration_bt = end_time_bt - start_time_bt
        #yeah bruh
        # Print the duration for each data structure
        print(f"Hash Table insertion time: {duration_ht} ns")
        print(f"B-Tree insertion time: {duration_bt} ns\n")





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

    def search_selected_crime_type(self):
        selected_type = self.selected_crime_type.get()
        if selected_type:
            self.search_crime_type(selected_type)

    def search_crime_type(self, crime_type):
        search_method = self.search_method_var.get()
        if search_method == "hash_table":
            self.search_crime_type_hash_table(crime_type)
        elif search_method == "b_tree":
            self.search_crime_type_b_tree(crime_type)
    
    def search_crime_type_hash_table(self, crime_type):
        selected_date = self.date_entry.get()
        selected_date_obj = None
        if selected_date:  # Check if a date is entered
            try:
                selected_date_obj = pd.to_datetime(selected_date).date()
            except ValueError:
                messagebox.showerror("Invalid Date", "Enter the date in YYYY-MM-DD format or leave blank")
                return

        start_time_ns = time.perf_counter_ns()
        results = []
        for bucket in self.hash_table.table:
            for key, record in bucket:
                record_date = pd.to_datetime(record['date']).date() if 'date' in record else None
                if record['primary_type'].lower() == crime_type.lower() and (not selected_date_obj or record_date == selected_date_obj):
                    results.append(record)
        end_time_ns = time.perf_counter_ns()
        search_duration_ns = end_time_ns - start_time_ns

        print(f"Hash table search time: {search_duration_ns} ns")
        print(f"Number of results found: {len(results)}\n")

        if results:
            results_df = pd.DataFrame(results)
            self.display_data(results_df)
        else:
            messagebox.showinfo("No results", "No matching records found.")


    def search_crime_type_b_tree(self, crime_type):
        selected_date = self.date_entry.get()
        selected_date_obj = None
        if selected_date:  # Check if a date is entered
            try:
                selected_date_obj = pd.to_datetime(selected_date).date()
            except ValueError:
                messagebox.showerror("Invalid Date", "Enter the date in YYYY-MM-DD format or leave blank")
                return

        start_time_ns = time.perf_counter_ns()
        results = []
        all_results = self.b_tree.search(crime_type.lower())  # Assuming this returns a list of records
        for record in all_results:
            record_date = pd.to_datetime(record['date']).date() if 'date' in record else None
            if not selected_date_obj or record_date == selected_date_obj:
                results.append(record)
        end_time_ns = time.perf_counter_ns()
        search_duration_ns = end_time_ns - start_time_ns

        print(f"B-tree search time: {search_duration_ns} ns")
        print(f"Number of results found: {len(results)}\n")

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

        reverse = self.sort_order.get(col, False)
        data_list = [(tree.set(k, col), k) for k in tree.get_children('')]

        #Sorting for districts
        if col == 'district':
            data_list.sort(key=lambda x: int(x[0]), reverse=reverse)

        else:
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
        print(f"Sorting time for column '{col}': {time_diff_ns} nanoseconds\n")  # Displaying the time taken in nanoseconds






    # Implement similar methods for other search options

def main():
    root = tk.Tk()
    app = CrimeDataApp(root)
    app.fetch_and_process_data()  # Load data into structures
    root.mainloop()


if __name__ == "__main__":
    main()
