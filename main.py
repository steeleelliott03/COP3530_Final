import tkinter as tk
from tkinter import ttk, messagebox
from data import fetch_data
from HashTable import HashTable
from Btree import BTree

class CrimeDataApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Data Analysis")
        self.root.geometry("600x400")  # Set the size of the window (width x height)

        # Initialize hash table and B-tree
        self.hash_table = HashTable()
        self.b_tree = BTree()

        # Create main menu buttons
        self.create_main_menu()


    def create_main_menu(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        btn_crime_type = tk.Button(main_frame, text="Search by Crime Type", command=self.open_crime_type_search)
        btn_crime_type.pack(fill='x', padx=5, pady=5)

        # Add other buttons similarly


    def fetch_and_process_data(self):
        data = fetch_data()
        for index, row in data.iterrows():
            key = row['district']  # Example key
            self.hash_table.insert(key, row.to_dict())  # Convert row to dictionary
            self.b_tree.insert(key, row.to_dict())


    # Define other methods for sub-menus, data display, etc.
    def create_main_menu(self):
        btn_crime_type = tk.Button(self.root, text="Search by Crime Type", command=self.open_crime_type_search)
        btn_crime_type.pack(fill='x')

        # Repeat for other buttons

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
        # Example: Searching the hash table for a specific crime type
        results = []
        for key in self.hash_table.keys():
            if self.hash_table.get(key)['primary_type'] == crime_type:
                results.append(self.hash_table.get(key))
        if results:
            self.display_data(results)
        else:
            messagebox.showinfo("No results", "No matching records found.")

    
    def display_data(self, data):
        display_window = tk.Toplevel(self.root)
        display_window.title("Search Results")
        display_window.geometry("800x600")  # Adjust size as needed

        tree_frame = tk.Frame(display_window)
        tree_frame.pack(fill='both', expand=True)

        tree = ttk.Treeview(tree_frame, columns=("district", "primary_type", "description"), show='headings')
        
        # Define the columns
        for col in tree["columns"]:
            tree.column(col, width=100)
            tree.heading(col, text=col.title())

        # Insert data into the treeview
        for index, row in data.iterrows():
            tree.insert("", "end", values=(row["district"], row["primary_type"], row["description"]))

        tree.pack(side='left', fill='both', expand=True)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        for item in data:
            tree.insert("", "end", values=(item["district"], item["primary_type"], item["description"]))




    # Implement similar methods for other search options

def main():
    root = tk.Tk()
    app = CrimeDataApp(root)
    app.fetch_and_process_data()  # Load data into structures
    root.mainloop()


if __name__ == "__main__":
    main()
